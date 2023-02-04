def Poly(convert):
    if convert == convert[::-1]:
        return True
    return False
       
userinput = input("Write polindrome: ")
if userinput == "exit":
    print("You selected",userinput)
    exit
else:
    userinput = userinput.lower()
    convert =""
    for strings in userinput:
        if strings.isalnum():
            convert += strings
print("Palindrome test:", Poly(convert))