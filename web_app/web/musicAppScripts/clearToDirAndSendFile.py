import math
import shutil
from optparse import OptionParser
from shutil import copyfile
import os, sys, random

COUNT = 20

def validateFileName(fileName):
    if fileName[0] == ".":
        return False
    if fileName[len(fileName)-3:len(fileName)] == "mp4" :
        return True
    if fileName[len(fileName)-3:len(fileName)] == "mp3":
        return True
    if fileName[len(fileName) - 3:len(fileName)] == "m4a":
        return True
    return True

def songListGen(dir, COUNT=20, typ=None):
    copyFiles = []
    nameCount = 1
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if typ is None:
                if validateFileName(file):
                    subdirect = os.path.join(subdir, file)
                    if not os.path.isdir(subdirect):
                        copyFiles.append(subdirect)
                        nameCount += 1
            else:
                if validateFileName(file) and file[len(file) - 3:len(file)] == typ:
                    subdirect = os.path.join(subdir, file)
                    if not os.path.isdir(subdirect):
                        copyFiles.append(subdirect)
                        nameCount += 1
            size = len(copyFiles)
    print (size)
    final_list = []
    for i in range(COUNT):
        index = int(math.floor(random.random() * (size - i)))
        songName = copyFiles.pop(index)
        final_list.append(songName)
    return final_list

def clear(dir):
    for file_path in list(os.listdir(dir)):
        if os.path.isfile(os.path.join(dir,file_path)):
            os.unlink(os.path.join(dir,file_path))
        elif os.path.isdir(os.path.join(dir,file_path)):
            shutil.rmtree(os.path.join(dir,file_path))

def sendFile(dirFrom, dirTo, dryrun, typ=None):
    lis = []
    file_names = []
    for subdir, dirs, files in os.walk(dirFrom):
            for file in files:
                if file[0] != ".":
                    lis.append(os.path.join(subdir, file))
                    file_names.append(file)
    size = len(lis)
    itertations = 0
    if COUNT < size:
        itertations = COUNT
    else:
        itertations = size
    if dryrun == True:
        final_list = songListGen(dirFrom,itertations,typ)
        for count, song in enumerate(final_list):
            copyfile(song, os.path.join(dirTo, str(count +1) + "." + song[len(song)-3:len(song)]))
        print (songListGen(dirFrom,typ=typ))
    else:
        print (songListGen(dirFrom,typ=typ))

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-r', '--dryrun', dest='dryrun', help='do a dry run',
                      default=True)

    (options, args) = parser.parse_args()

    dryrun = options.dryrun
    dirFrom = raw_input("From directory :")
    dirTo = raw_input("To directory :")
    typ = raw_input("Type of file: (Blank or type)")
    clear(dirTo)
    if typ != "":
        sendFile(dirFrom, dirTo, dryrun,typ)
    else:
        sendFile(dirFrom, dirTo, dryrun)

