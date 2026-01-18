from database import create_table, connect_db

create_table()

def add_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    subject = input("Enter Subject: ")
    marks = int(input("Enter Marks: "))

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students VALUES (?,?,?,?)",
                (roll, name, subject, marks))
    conn.commit()
    conn.close()
    print("Student added successfully!")

def view_students():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()

    print("\nRoll | Name | Subject | Marks")
    print("-"*30)
    for row in rows:
        print(row)

def delete_student():
    roll = int(input("Enter Roll No to delete: "))
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE roll_no=?", (roll,))
    conn.commit()
    conn.close()
    print("Student deleted successfully!")

def menu():
    while True:
        print("\n--- Student Result Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

menu()