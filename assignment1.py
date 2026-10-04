"""
Assignment 1: Student Data Management Using Python Collections

Write a Python program to create and store student information using a
Dictionary, Tuple, and List. Perform the following operations on the
Dictionary:
    1. Add a new student record.
    2. Delete an existing student record.
    3. Update the details of a student.
    4. Display the final student records after performing all the operations.

Use suitable student attributes such as Roll Number, Name, Branch, and Marks.
"""


students = {
    101: ("Amit", "CSE", 85),
    102: ("Neha", "IT", 90),
}


def display_records(students):
    
    records = list(students.items())
    print("\n{:<8}{:<15}{:<10}{:<8}".format("Roll", "Name", "Branch", "Marks"))
    print("-" * 41)
    for roll, (name, branch, marks) in records:
        print("{:<8}{:<15}{:<10}{:<8}".format(roll, name, branch, marks))


def main():
    while True:
        print("\n1. Add  2. Delete  3. Update  4. Display final records  5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            roll = int(input("Roll Number: "))
            if roll in students:
                print("Roll number already exists!")
            else:
                name = input("Name: ")
                branch = input("Branch: ")
                marks = float(input("Marks: "))
                students[roll] = (name, branch, marks)
                print("Record added.")

        elif choice == "2":
            roll = int(input("Roll Number to delete: "))
            if roll in students:
                del students[roll]
                print("Record deleted.")
            else:
                print("Record not found.")

        elif choice == "3":
            roll = int(input("Roll Number to update: "))
            if roll in students:
                name, branch, marks = students[roll]
                # Tuples are immutable, so we build a new tuple
                new_name = input(f"Name [{name}]: ") or name
                new_branch = input(f"Branch [{branch}]: ") or branch
                new_marks = input(f"Marks [{marks}]: ")
                new_marks = float(new_marks) if new_marks else marks
                students[roll] = (new_name, new_branch, new_marks)
                print("Record updated.")
            else:
                print("Record not found.")

        elif choice == "4":
            display_records(students)

        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
