import subprocess
qrelFile = "trec_rel_file"                    #for testing - should be path to qrel file
resFile = "trec_top_file"                     #for testing - should be path to res file
p = subprocess.Popen("trec_eval " + qrelFile + " " + resFile, stdout=subprocess.PIPE, shell=True)   #calls trec_eval with arguments specified above
(output, err) = p.communicate()
output = output.replace(" ","")               #removes spaces
output = output.split("\n")                   #splits output into list - 1 string for every line
for i in range(0,len(output)):
    if "Averageprecision" in output[i]:     
        MAP = output[i+1]                     #MAP value is the next item in list
        MAP = MAP[:-1]                        #trim return character
    if "At10docs" in output[i]:
        p10 = output[i][9:-1]                 #trims string and removes return character  
    if "At20docs" in output[i]:
        p20 = output[i][9:-1]                 #trims string and removes return character
values={"MAP" : MAP, "p10" : p10, "p20" : p20}
print values


