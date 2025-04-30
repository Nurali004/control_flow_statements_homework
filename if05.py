def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    return (a<0)+(b<0)+(c<0)

a=int(input("sonni kiriting:"))
b=int(input("sonni kiriting:"))
c=int(input("sonni kiriting:"))
print(main(a,b,c))