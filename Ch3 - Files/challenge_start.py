# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import os
totalsize = 0
listdir = os.listdir()
for item in listdir:
    if os.path.isfile(item):
        fsize = os.path.getsize(item)
        totalsize = totalsize + fsize
os.mkdir("results")
rfile = open("results/rfile.txt", "w+")
rfile.write("Total size: " + str(totalsize) + " bytes\n\n")
for item in listdir:
    if os.path.isfile(item):
        rfile.write(item + "\n")
rfile.close

