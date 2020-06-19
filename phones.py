from os import listdir
from os.path import isfile, join
import sys, os

data_name = "polish"
mypath = os.path.abspath(os.path.split(sys.argv[0])[0])
print(mypath)
path = mypath+"/data/local/dict/"

with open(path+"lexicon.txt", encoding="utf8") as f:
    lines = f.read().splitlines()[2:]
    print(lines)

phonemas = set()

for item in lines:
    ph = item.split('\t')[1].split(' ')
    print(ph)
    phonemas.update(ph)
    print(phonemas)
    
phonemas_list = list(phonemas)
with open(path + "nonsilence_phones.txt", "w", encoding="utf8") as outfile:
    outfile.write("\n".join(phonemas_list))
silence = ['sil', 'spn']   
opt_silence = ['sil'] 
with open(path + "silence_phones.txt", "w", encoding="utf8") as outfile:
    outfile.write("\n".join(silence))
with open(path + "optional_silence.txt", "w", encoding="utf8") as outfile:
    outfile.write("\n".join(opt_silence))