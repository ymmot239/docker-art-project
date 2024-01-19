from os import listdir
import os
#import win32com.client
from os.path import isfile, join
import re, random

def get_file_metadata(path, filename, metadata, index):
    # Path shouldn't end with backslash, i.e. "E:\Images\Paris"
    # filename must include extension, i.e. "PID manual.pdf"
    # Returns dictionary containing all file metadata.
    sh = win32com.client.gencache.EnsureDispatch('Shell.Application', 0)
    ns = sh.NameSpace(path)

    # Enumeration is necessary because ns.GetDetailsOf only accepts an integer as 2nd argument
    file_metadata = dict()
    item = ns.ParseName(str(filename))
    print(item)
    for ind, attribute in enumerate(metadata):
        attr_value = ns.GetDetailsOf(item, index)
        if attr_value:
            file_metadata[attribute] = attr_value

    return file_metadata

def read_new(file_name):
    file = open(file_name,"r")
    metadata = ['Genre']
    holder = file.readlines()
    path = 'C:\\Users\\pacma\\Downloads\\art\\docker-art-project\\art-project-main\\music\\Classical Guitar'
    for x in holder:
        print(get_file_metadata(path,x[:-1],metadata, 16))
    
    return holder
    
def get_music():
    mypath = "../music"
    filelist = next(os.walk(mypath))[1]
    onlyfiles = {}
    for x in filelist:
        newpath = mypath + "/" + x
        #onlyfiles += [newpath + "/" + f for f in listdir(newpath) if isfile(join(newpath, f))]
        for f in listdir(newpath):
             if isfile(join(newpath,f)):
                 f_edit = re.sub(r'[^a-zA-Z\d\s:]',"",f[:-4]).strip()
                 if len(f_edit) > 30:
                     f_edit = f_edit[:30] + "~"
                 onlyfiles[f_edit] = [newpath+"/"+f,x]
    return onlyfiles

def recommend_number():
    pass

def export_changes():
    pass


if __name__ == "__main__":
   # read_new("test.txt")
    List = get_music()
    file = open("genre_to_song.txt", "w+", encoding="utf-8")
    for key in List:
        file.write(List[key][1]+" : "+key+"\n")
    file.close()
    file = open("song_to_path.txt", "w+", encoding="utf-8")
    for key in List:
        file.write(key + " : " + List[key][0] + "\n")

    
