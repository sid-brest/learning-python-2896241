# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = "abc"
print(myint)
# to access a member of a sequence type, use []
print(mylist[2])
# use slices to get parts of a sequence
print(mylist[1:5])
print(mylist[1:5:2])
# you can use slices to reverse a sequence
print(mylist[::-1])
# dictionaries are accessed via keys
print(mydict["two"])
# ERROR: variables of different types cannot be combined
print(mystr + " " + str(123))
# Global vs. local variables in functions
def func():
    global mystr
    mystr = "def"
    print(mystr)

func()
print(mystr)

del mystr   

thestr = "Ogres are often foolhardy oafs"
newstr = ""
for i, c in enumerate(thestr):
    if c == "o":
        continue
    if i > 20:
        break
    newstr += c
print(newstr)

var="123456789"
print(var[1:6:2])

value=input("2+2=")
