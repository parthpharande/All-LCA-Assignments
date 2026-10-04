"""
Assignment 3: Write a python program that accepts the length of three sides
of a triangle as inputs. The program should indicate whether or not the
triangle is a right-angled triangle using a function.
"""


def is_right_angled(a, b, c):
    x, y, z = sorted([a, b, c])             # z is the longest side
    return x > 0 and abs(x**2 + y**2 - z**2) < 1e-9


def main():
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))

    if is_right_angled(a, b, c):
        print("The triangle is a right-angled triangle.")
    else:
        print("The triangle is NOT a right-angled triangle.")


if __name__ == "__main__":
    main()
