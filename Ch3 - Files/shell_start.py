#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists("testfile.txt"):
        # get the path to the file in the current directory
        source = path.realpath("testfile.txt")
        # let's make a backup copy by appending "bak" to the name
        destination = source + ".bak"
        # rename the original file
        shutil.copy(source,destination)
        os.rename("testfile.txt", "newfile.txt")
        # now put things into a ZIP archive
        # root_dir,tail = path.split(source)
        # shutil.make_archive("archive", "zip", root_dir)
        # more fine-grained control over ZIP files
        with ZipFile("testfile.zip","w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("testfile.txt.bak")

      
if __name__ == "__main__":
    main()
