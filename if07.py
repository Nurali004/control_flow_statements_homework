def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a==0:
        return "zero"
    elif a>0 and a%2==0:
        return "juft raqam"
    elif a>0 and a%2==1:
        return "toq musbat raqam"

    elif a<0 and a%2==0:
        return "juft manfiy raqam"
    else:
        return "manfiy toq raqam"

a=int(input("sonni kiriting:"))
print(main(a))
