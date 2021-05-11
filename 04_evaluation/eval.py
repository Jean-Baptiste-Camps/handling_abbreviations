import fastwer
import glob
import pandas


def compute_score(gt, folder):
    """
    :param gt: address of the file containing gt
    :param folder: folder containing hypotheses to test
    :return: a panda data frame with scores
    """
    with open(gt, 'r') as f:
        gt = f.readlines()

    # gt2 = gt
    hypotheses = {}
    for eval in glob.glob(evals):
        with open(eval, 'r') as f:
            hypotheses[eval] = f.readlines()

    CERs = []
    WERs = []
    keys = hypotheses.keys()

    for key in keys:
        CERs.append(fastwer.score(hypotheses[key], gt, char_level=True))
        WERs.append(fastwer.score(hypotheses[key], gt))

    d = {'CER': CERs, 'WER': WERs}

    return pandas.DataFrame(data=d, index=keys)


if __name__ == "__main__":
    gt = "gt_fol11_nopunct.txt"
    evals = "to_eval/*"

    df = compute_score(gt, evals)
    df.to_csv("eval.csv")
