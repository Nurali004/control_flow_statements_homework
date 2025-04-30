def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    neg=(a>0)+(b>0)+(c>0)
    pos=(a<0)+(b<0)+(c<0)
    if neg>pos:
        return "there are alot of positive numbers"
    elif neg<pos:
        return "there are a lot of negative numbers"
    else:
        return "it is not equal"

a=int(input("sonni kiriting:"))
b=int(input("sonni kiriting:"))
c=int(input("sonni kiriting:"))
print(main(a,b,c))