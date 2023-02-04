#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I am a func1")
# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)
# TODO: function that returns a value
def func3(x):
    return x * x * x
# TODO: function with default value for an argument
def func4(num, x=1):
    result = 1
    for i in range (x):
        result = result * num
    return result
# TODO: function with variable number of arguments
def func5(*args):
    result = 0
    for i in args:
        result = result + i
    return result

func1()
func2(20,40)
print(func3(5))
print(func4(5))
print(func4(5,5))
print(func4(x=3, num=5))
print(func5(3,45,5))

def inc(a,b=1):
    return(a+b)
a=inc(1)
a=inc(a,a)
print(a)