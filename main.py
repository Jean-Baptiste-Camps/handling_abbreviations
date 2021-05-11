#import boudams
#import boudams.cli
import glob
from boudams.tagger import BoudamsTagger
import re
import tqdm
# Get output

### Process calfa without spaces

with open("01_htr/output/calfa-developpe_sans-espace_p48.txt") as f:
    calfa = f.read().replace('\n', '').replace('/', '')

with open("02_segmentation/input/calfa-developpe_sans-espace_p48.txt", 'w') as f:
    f.write(calfa)

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

