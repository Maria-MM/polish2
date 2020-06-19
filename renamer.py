from os import listdir
from os.path import isfile, join
import sys, os



def get_names(path):
    speakers = [f for f in listdir(path)]
    return speakers
    #onlyfiles = [f for f in listdir(path) if f.endswith(".wav") ]
speakers = get_names("/home/student/snuv/snuv/snuv_database")

def rename(spk_list, path):

    for item in spk_list:
        onlyfiles= [f for f in listdir(path+"/"+item)]
        for el in onlyfiles:
            os.rename(path+"/"+item+"/"+el, path+"/"+item+"/"+item+"_"+el)
            
            
rename(speakers, "/home/student/snuv/snuv/snuv_database")
