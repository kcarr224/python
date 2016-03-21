#!/usr/bin/env python
import glob
import os
import tarfile
import zipfile

def FindBundleRootDirs(dir):
    bundleDirs = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if "PUBLIC" in file:
                bundleDirs.append(root)
    return bundleDirs

def FindPublicBundle(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if "PUBLIC_" in file:
                return file 

def FindFile(dir, fileName):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if fileName in file:
                return os.path.join(root, file)     
    return

def AddFileSize(myfile, dir, fileName):
    filePath = FindFile(dir, fileName)    
    if not filePath:
        myfile.write("missing")
    else:
        statinfo = os.stat(filePath)
        fileSize =statinfo.st_size
        myfile.write(str(fileSize))


def AddWonW(myfile, dir):
    filePath = FindFile(dir, "bitecollector_report.log")    
    if not filePath:
        myfile.write("missing\n")
    else:
        bcFile = open(filePath, "r")
        for line in bcFile:
            if "fdfDiscreteWeightOnWheels;\"1\"" in line:
                myfile.write(line)
                return
        return myfile.write("WoW not found\n") 

def AddIfeService(myfile, dir):
    filePath = FindFile(dir, "bitecollector_report.log")    
    if not filePath:
        myfile.write("missing")
    else:
        bcFile = open(filePath, "r")
        for line in bcFile:
            if "ifeServiceStatus;\"2\";" in line:
                print "ife:  " + line
                myfile.write("true")
                return
        return myfile.write("false") 

def DateFromArchive(archiveName):
    tags=archiveName.split('_')
    print tags
    rollDate=tags[3]
    print rollDate
    return rollDate


def NewResultFile(csvFileName):
    myfile = open(csvFileName, "w")
    myfile.write("Flight Date,PUBLIC Archive,PAX Usage File Size,Flight Summary File Size,IFE Service Available,Bite Collector WonW\n")
    bundleDirs = FindBundleRootDirs(".")
    for dir in bundleDirs:
        print dir
        publicArchive = FindPublicBundle(dir)
        flightDate = DateFromArchive(publicArchive)
        myfile.write(flightDate)
        myfile.write(',')
        myfile.write(publicArchive)
        myfile.write(',')
        AddFileSize(myfile, dir, "paxUsage.csv")
        myfile.write(',')
        AddFileSize(myfile, dir, "flightSummary.csv")
        myfile.write(',')
        AddIfeService(myfile, dir)
        myfile.write(',')
        AddWonW(myfile, dir)

NewResultFile("BAG.csv")
