#!/usr/bin/env python
import glob
import os
import tarfile
import zipfile
import re


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError:  # Python >2.5
        print "Dir exist: " + path


def ExtractBundles(archiveRootDir):
    sourceArchives=archiveRootDir + '/'  + "ziide*.tar.gz"
    print sourceArchives
    tgzFiles = glob.glob(sourceArchives)
    print tgzFiles
    for file in tgzFiles:
        print file
        tags=file.split('_')
        print tags
        rollDate=tags[1]
        print rollDate
        id=tags[2]
        print id
        dir=rollDate + '/' + id
        print dir
        mkdir_p(dir)
        filePath=dir + '/' + file
        os.rename(file, filePath)
        tar = tarfile.open(filePath)
        tar.extractall(dir)

def findMatch(pattern):
    folders = []
    rePattern = re.compile(pattern)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if rePattern.match(name):
                print(name) 
                print(root)
                folders.append(root)
    return folders

#ExtractBundles(".")
def WalkAndExtract():
    pwd = os.getcwd()
    print pwd
    dirs = findMatch("ziide_*")
    for dir in dirs:
        print dir
        os.chdir(dir)
        print os.getcwd()
        print "call extract"
        ExtractBundles(".")
        os.chdir(pwd)
        print pwd
    
WalkAndExtract()
