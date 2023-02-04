#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)
    
    # Check for item existence and type
    print("Exist testfile " + str(path.exists("testfile.txt")))
    print("Exist file " + str(path.isfile("testfile.txt")))
    print("Exist clear dir " + str(path.isdir("testfile.txt")))

    
    # Work with file paths
    print("File path is " + str(path.realpath("testfile.txt")))

    
    # Get the modification time
    print("Modification time is " + time.ctime(path.getctime("testfile.txt")))

    
    # Calculate how long ago the item was modified
    timediff = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("testfile.txt"))
    print("It has been " + str(timediff) + " since the file was modified")

  
if __name__ == "__main__":
    main()
