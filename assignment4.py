"""
Assignment 4: Write a python program to create an array and perform
addition of two matrices.
"""


def read_matrix(name, rows, cols):
    print(f"Enter elements of matrix {name} row by row:")
    return [[int(input(f"{name}[{i}][{j}]: ")) for j in range(cols)]
            for i in range(rows)]


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    A = read_matrix("A", rows, cols)
    B = read_matrix("B", rows, cols)

    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

    print("\nSum of the matrices:")
    for row in result:
        print(*row)


if __name__ == "__main__":
    main()
