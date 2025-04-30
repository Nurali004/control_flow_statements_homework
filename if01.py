def main(a):
    """
    If the number is positive, increase it by 1, otherwise leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    if a > 0:
        return a + 1
    else:
        return a

# Foydalanuvchidan son kiritiladi
a = int(input("Sonni kiriting: "))
print(main(a))  # Natijani chiqarish





