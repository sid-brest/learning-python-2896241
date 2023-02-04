#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



from unittest import case


def main():
    x, y = 1070, 100

    # conditional flow uses if, elif, else
    if x < y:
        result1 = "x lower than y"
    elif x == y:
        result1 = "x equals y"
    else:
        result1 = "x greater than y"
    print(result1) 
    # conditional statements let you use "a if C else b"
    result2 = print ("x lower than y") if x < y else "x equals or greater than y"
    print(result2)
    # match-case makes it easy to compare multiple values
    value = "5"
    match value:
        case "one":
            result3 = 1
        case "two":
            result3 = 2
        case "three" | "four":
            result3 = (3,4)
        case _:
            result3 = "Another match"
    print(result3)

if __name__ == "__main__":
    main()