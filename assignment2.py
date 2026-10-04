"""
Assignment 2: Write a python program to find the largest of three numbers.
"""


def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest number is:", largest)


if __name__ == "__main__":
    main()
