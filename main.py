#import boudams
#import boudams.cli
import glob
from boudams.tagger import BoudamsTagger
import re
import shutil
import pie.scripts.tag
import tqdm
# Get output

### To process
### This one stays as is
shutil.copy("01_htr/output/calfa-developpe_avec-espace_p48.txt", "04_evaluation/to_eval/calfa-developpe_avec-espace_p48.txt")

### This one needs processing

htrout = ['01_htr/output/kraken-abrege_sans-espace_p48.txt',
          '01_htr/output/calfa-developpe_sans-espace_p48.txt']

for file in htrout:
    with open(file, 'r') as f:
        cleaned = f.read().replace('\n', '').replace('/', '')

    with open(file.replace("01_htr/output/", "02_segmentation/input/"), 'w') as f:
        f.write(cleaned)

######## Segment all

for model in glob.glob("02_segmentation/models/*"):
    modelname = model.split("/")[-1]
    model = BoudamsTagger.load(model, device="cpu")
    remove_line = True
    spaces = re.compile("\s+")
    apos = re.compile("['’]")
    for file in glob.glob("02_segmentation/input/*"):
        out_name = file.replace(".txt", ("."+modelname+".txt")).replace("02_segmentation/input/", "02_segmentation/output/")

        with open(file, 'r') as f:
            content = f.read()

        if remove_line:
            content = spaces.sub("", content)

        # Now, extract apostrophes, remove them, and reinject them
        apos_positions = [i for i in range(len(content)) if content[i] in ["'", "’"]]
        content = apos.sub("", content)

        with open(out_name, "w") as out_io:
            out = ''
            for tokenized_string in model.annotate_text(content, batch_size=32):
                out = out + tokenized_string + " "

            # Reinject apostrophes
            true_index = 0
            for i in range(len(out) + len(apos_positions)):
                if true_index in apos_positions:
                    out = out[:i] + "'" + out[i:]
                    true_index = true_index + 1
                else:
                    if not out[i] == ' ':
                        true_index = true_index + 1

            out_io.write(out)

### Now, we are done for Calfa files

for file in glob.glob("02_segmentation/output/calfa-developpe_sans-espace_p48.0*"):
    shutil.copy(file,file.replace("02_segmentation/output/", "04_evaluation/to_eval/"))

### We can proceed to normalisation for the others

for file in glob.glob("02_segmentation/output/kraken*"):
    shutil.copy(file,file.replace("02_segmentation/output/", "03_normalisation/input/"))

files = glob.glob("03_normalisation/input/*")

for model in glob.glob("03_normalisation/models/*"):
    modelspec = '"<'+model+",normalised>"''
    pie.scripts.tag.run(modelspec, files, beam_width=10, use_beam=True, keep_boundaries=True, device="cpu", batch_size=50, lower=False, max_sent_len=35, vrt=True)