#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
# x = 10 / 0
# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
try:
    x = 10 / 0
except: 
    print("It doesn't work!")
# TODO: You can also catch specific exceptions
try:
    num = input("Enter mumber ")
    y = int(num)
    z = 10 / y
    print(z)
except ZeroDivisionError as e:
    print("You can't divide by zero!")
except ValueError as e:
    print("You didn't give me a valid number!", e)
finally:
    print("The finally section always runs")
    
