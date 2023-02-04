#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0
    i = 0
    k = 0

    # TODO: define a while loop
    while (x < 5):
        print(x)
        x = x + 1  
    # TODO: define a for loop
    for i in range (10,20):
        print(i)
    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for d in days:
        print(d)
    # TODO: use the break and continue statements
    for k in range (10,50):
        if k > 16:
            break
        elif k % 2 == 0:
            continue
    print(i)
    # TODO: using the enumerate() function to get index 
    for i, d in enumerate(days):
        print (i, d)
 
if __name__ == "__main__":
    main()
