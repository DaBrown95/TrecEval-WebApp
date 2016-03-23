import subprocess
import os
from TrecEval.settings import BASE_DIR, RUN_FILES

#if os.name == 'nt':
#    TREC_PATH = os.path.join(BASE_DIR, 'TrecApp/trec_eval_dos')
#elif os.name == 'posix':

TREC_PATH = os.path.join(BASE_DIR, 'TrecApp/trec_eval_macosx')
#TREC_PATH = os.path.join(BASE_DIR, 'TrecApp/trec_eval_linux')



def trec_eval(qRel, res, debug=False):

    if not debug:
        filepath = os.path.join(BASE_DIR, 'media/processingFile.txt')
        with open(filepath, 'w') as dest:
            for chunk in res.chunks():
                dest.write(chunk)

        res = filepath

    p = subprocess.Popen(TREC_PATH + " " + qRel + " " + res, stdout=subprocess.PIPE,
                         shell=True)  # calls trec_eval with arguments specified above
    (output, err) = p.communicate()
    output = output.split("\n")
    print output
    values = {"MAP": output[5][-6:], "p10": output[22][-6:], "p20": output[24][-6:]}
    print values
    return values