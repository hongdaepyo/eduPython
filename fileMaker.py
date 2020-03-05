import os, sys, subprocess

def makeTestFiles(num):
    tmpPath = "c://kidpmig/test/"
    for i in range(num):
        subprocess.Popen(["echo", "1", ">>", tmpPath + str(i) + ".txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return

makeTestFiles(500)