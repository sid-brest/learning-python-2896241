#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    file1 = open("testfile.txt", "w+")
        
    # write some lines of data to the file
    for i in range(10):
        file1.write("This is a text %d\n" % (i+1))
    
    # close the file when done
    file1.close
    
    # Open the file for appending text to the end
    file1 = open("testfile.txt", "a")
    for i in range(10):
        file1.write("This is a new text %d\n" % (i+1))
    file1.close

    # Open the file back up and read the contents
    file1 = open("testfile.txt", "r")
    if file1.mode == 'r':
        content = file1.read()
    print(content)
    
if __name__ == "__main__":
    main()
