import subprocess
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TREC_PATH = os.path.join(BASE_DIR, 'TrecApp/trec_eval_macosx')
RUN_FILES = os.path.join(BASE_DIR, 'media/runFiles')


def trec_eval(qRel, res):
    p = subprocess.Popen(TREC_PATH + " " + qRel + " " + res, stdout=subprocess.PIPE, shell=True)   #calls trec_eval with arguments specified above
    (output, err) = p.communicate()
    print output
    output = output.split("\n")
    values = {"MAP": output[5][-6:], "p10": output[22][-6:], "p20": output[24][-6:]}
    return values

