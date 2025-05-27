# main.py

import database

def menu():
    print("\n🎓 Student Grade Management System 🎓")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Grade")
    print("5. Delete Student")
    print("6. Exit")

def main():
    database.init_db()

    while True:
        menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter student name: ")
            roll_no = input("Enter roll number: ")
            subject = input("Enter subject: ")
            grade = input("Enter grade: ")
            database.add_student(name, roll_no, subject, grade)

        elif choice == '2':
            students = database.view_all_students()
            print("\n--- Student Records ---")
            for s in students:
                print(f"ID: {s[0]}, Name: {s[1]}, Roll No: {s[2]}, Subject: {s[3]}, Grade: {s[4]}")

        elif choice == '3':
            keyword = input("Enter name, roll number, or subject to search: ")
            results = database.search_students(keyword)
            print("\n--- Search Results ---")
            for r in results:
                print(f"ID: {r[0]}, Name: {r[1]}, Roll No: {r[2]}, Subject: {r[3]}, Grade: {r[4]}")

        elif choice == '4':
            roll_no = input("Enter roll number of student: ")
            subject = input("Enter subject: ")
            new_grade = input("Enter new grade: ")
            database.update_grade(roll_no, subject, new_grade)

        elif choice == '5':
            roll_no = input("Enter roll number to delete: ")
            database.delete_student(roll_no)

        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main()
