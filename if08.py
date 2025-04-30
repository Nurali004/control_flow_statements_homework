def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if 10<=a<=99:
     if a%2==0:
        return " musbat juft ikki xonali raqam"
     else:
        return "juft musbat ikki xonali raqam"
    elif -99<=a<=-10:
     if a%2==1:
        return "manfiy toq raqam"
     else:
        return "manfiy juft raqam"
    else:
        return "bunday son yo'q"

    
      
    

a=int(input("sonni kiriting:"))
print(main(a))