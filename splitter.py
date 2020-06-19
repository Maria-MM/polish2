from os import listdir
from os.path import isfile, join
import sys, os

data_name = "polish"
mypath = os.path.abspath(os.path.split(sys.argv[0])[0])
print(mypath)

def get_names(path):
    path_ = mypath + path;
    speakers = [f for f in listdir(path_)]
    return speakers
    #onlyfiles = [f for f in listdir(path) if f.endswith(".wav") ]
test_speakers = get_names("/polish_audio/test")
train_speakers = get_names("/polish_audio/train")

corpus = []

def write_spk2gender(spk_list, path):
    l = []
    
    for item in spk_list:
        gender = 'k' if ('k' in item.split('_')[0]) else 'm'
        l.append(item+" "+gender)
    with open(os.path.join(mypath+"/data/"+path,"spk2gender"), "w", encoding="utf8") as outfile:
        outfile.write("\n".join(l))
def write_another(spk_list, path):
    l = [] 
    lt = []
    lu = []
    for item in spk_list:
        onlyfiles = [f for f in listdir(mypath+"/"+data_name+"_audio/"+path+"/"+item) if f.endswith(".wav") ]
        for el in onlyfiles:
            wav_name = el.split('.')[0]
            l.append(item+"-"+wav_name+" "+mypath+"/"+data_name+"_audio/"+path+"/"+item+"/"+el)
            with open(mypath+"/"+data_name+"_audio/"+path+"/"+item+"/"+wav_name+".txt", 'r') as file:
                data = file.read().replace('\n', '')
            corpus.append(data)
            #data = filter(lambda ch: ch not in "()", data)
            lt.append(item+"-"+wav_name+" "+data)
            lu.append(item+"-"+wav_name+" "+item)
    #print(lt)
    with open(os.path.join(mypath+"/data/"+path,"wav.scp"), "w", encoding="utf8") as outfile:
        outfile.write("\n".join(l))
    #print("utt2spk len: " +str(len(lu)) + " vs text len: " + str(len(lt))
    with open(os.path.join(mypath+"/data/"+path,"text"), "w", encoding="utf8") as outfile:
        outfile.write("\n".join(lt))
    with open(os.path.join(mypath+"/data/"+path,"utt2spk"), "w", encoding="utf8") as outfile:
        outfile.write("\n".join(lu))    
write_spk2gender(test_speakers, "test")
write_spk2gender(train_speakers, "train")
write_another(test_speakers, "test")
write_another(train_speakers, "train")
with open(os.path.join(mypath+"/data/local/","corpus.txt"), "w") as outfile:
        outfile.write("\n".join(corpus))

