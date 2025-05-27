# database.py

import sqlite3

# Initialize the database
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT NOT NULL UNIQUE,
            subject TEXT NOT NULL,
            grade TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Add a new student
def add_student(name, roll_no, subject, grade):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (name, roll_no, subject, grade) VALUES (?, ?, ?, ?)",
                       (name, roll_no, subject, grade))
        conn.commit()
        print("✅ Student added successfully.")
    except sqlite3.IntegrityError:
        print("❌ Error: Roll number must be unique.")
    conn.close()

# View all students
def view_all_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Search for students
def search_students(keyword):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ? OR roll_no LIKE ? OR subject LIKE ?",
                   (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
    results = cursor.fetchall()
    conn.close()
    return results

# Update student grade
def update_grade(roll_no, subject, new_grade):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade = ? WHERE roll_no = ? AND subject = ?", 
                   (new_grade, roll_no, subject))
    conn.commit()
    if cursor.rowcount > 0:
        print("✅ Grade updated successfully.")
    else:
        print("❌ No matching student found.")
    conn.close()

# Delete a student
def delete_student(roll_no):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
    conn.commit()
    if cursor.rowcount > 0:
        print("✅ Student deleted successfully.")
    else:
        print("❌ No student found with that roll number.")
    conn.close()
