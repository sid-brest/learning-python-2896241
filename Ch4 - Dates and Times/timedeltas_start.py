#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

today = date.today()

 # Option A:
tomorrow1 = date.today()
 # Option B:
tomorrow2 = date(today.year,today.month,today.day+1)
print(tomorrow1)
print(tomorrow2)

texpdate = date.today()
if ((texpdate.today()).days<7):
    print("password will expire soon!")


# TODO: construct a basic timedelta and print it


# TODO: print today's date


# TODO: print today's date one year from now


# TODO: create a timedelta that uses more than one argument


# TODO: calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?


# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# TODO: Now calculate the amount of time until April Fool's Day  

