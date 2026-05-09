# Student Grade Management System
# --------------------------------
# Features:
# 1. Add Student
# 2. View All Students
# 3. Search Student
# 4. Update Marks
# 5. Delete Student
# 6. Calculate Grade
# 7. Exit

students = {}


def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def add_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    marks = []

    subjects = ["Math", "Science", "English"]

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    students[roll_no] = {
        "name": name,
        "marks": marks,
        "average": average,
        "grade": grade
    }

    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n--- Student Records ---")
    for roll_no, data in students.items():
        print(f"Roll No: {roll_no}")
        print(f"Name: {data['name']}")
        print(f"Marks: {data['marks']}")
        print(f"Average: {data['average']:.2f}")
        print(f"Grade: {data['grade']}")
        print("-" * 30)


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no in students:
        data = students[roll_no]
        print("\nStudent Found!")
        print(f"Name: {data['name']}")
        print(f"Marks: {data['marks']}")
        print(f"Average: {data['average']:.2f}")
        print(f"Grade: {data['grade']}\n")
    else:
        print("Student not found.\n")


def update_marks():
    roll_no = input("Enter Roll Number to update: ")

    if roll_no not in students:
        print("Student not found.\n")
        return

    subjects = ["Math", "Science", "English"]
    new_marks = []

    for subject in subjects:
        mark = float(input(f"Enter new marks for {subject}: "))
        new_marks.append(mark)

    average = sum(new_marks) / len(new_marks)
    grade = calculate_grade(average)

    students[roll_no]["marks"] = new_marks
    students[roll_no]["average"] = average
    students[roll_no]["grade"] = grade

    print("Marks updated successfully!\n")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


def menu():
    while True:
        print("\n===== Student Grade Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using Student Grade Management System!")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
menu()
