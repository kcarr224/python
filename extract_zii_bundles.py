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


def ExtractBundles(archiveRootDir):
    sourceArchives=archiveRootDir + '/'  + "ziide*.tar.gz"
    tgzFiles = glob.glob(sourceArchives)
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


ExtractBundles(".")

