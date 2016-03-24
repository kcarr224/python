#!/usr/bin/env python
import glob
import os
import tarfile
import zipfile



def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError:  # Python >2.5
        print "Dir exist: " + path

def ExtractBundles(archiveRootDir, type):
    sourceArchives=archiveRootDir + '/' + type + "*.tgz"
    tgzFiles = glob.glob(sourceArchives) 
    for file in tgzFiles:
        print file
        tags=file.split('_')
        print tags
        rollDate=tags[3]
        print rollDate
        id=tags[4]
        print id
        dir=rollDate + '/' + id    
        print dir
        mkdir_p(dir)
        filePath=dir + '/' + file
        os.rename(file, filePath)
        print "Extract: " + filePath
        tar = tarfile.open(filePath)
        tar.extractall(dir)

def ExtractZip(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".zip"):
                zipDir=root
                print zipDir
                zipPath=os.path.join(root,file)
                print zipPath
                zf = zipfile.ZipFile(zipPath, "r")
                zf.extractall(zipDir)
                #os.remove(zipPath)

def ExtractTgz(dir, ext):
    print dir
    print ext
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(ext):
                outDir=root
                print outDir
                tgzPath=os.path.join(root,file)
                print tgzPath
                tar = tarfile.open(tgzPath)
                tar.extractall(outDir)
                #os.remove(tgzPath)

ExtractBundles(".", "PRIVATE")
ExtractTgz(".", "*.tgz")
