import os
from dataclasses import dataclass

@dataclass
class Student:
    student_id: str
    first_name: str
    last_name: str
    class_standing: float
    major_exam: float

    def final_grade(self):
        return (self.class_standing * 0.6) + (self.major_exam * 0.4)

def load_records(filename):
    records = []
    if not os.path.exists(filename):
        print('File not found. Starting with an empty record.')
        return records
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                records.append(Student(parts[0], parts[1], parts[2], float(parts[3]), float(parts[4])))
    except Exception as e:
        print(f"Error loading file: {e}")
    return records

def save_records(records, filename):
    try:
        with open(filename, 'w') as file:
            for record in records:
                file.write(f'{record.student_id},{record.first_name},{record.last_name},{record.class_standing},{record.major_exam}\n')
        print(f'Records saved to {filename}')
    except Exception as e:
        print(f"Error saving file: {e}")

def save_as_file(records):
    filename = input("Enter new filename: ")
    save_records(records, filename)

def display_records(records, sort_by="last_name"):
    if not records:
        print("No student records available.")
        return

    if sort_by == "grade":
        records.sort(key=lambda x: x.final_grade(), reverse=True)
    else:
        records.sort(key=lambda x: x.last_name)
    
    print(f"\n{'ID':<10}{'Name':<25}{'Class Standing':<15}{'Major Exam':<12}{'Final Grade':<12}")
    print("-" * 70)
    for r in records:
        print(f"{r.student_id:<10}{r.first_name + ' ' + r.last_name:<25}{r.class_standing:<15.2f}{r.major_exam:<12.2f}{r.final_grade():<12.2f}")

def add_record(records):
    student_id = input('Enter Student ID (6 digits): ').strip()
    if not student_id.isdigit() or len(student_id) != 6:
        print("Invalid ID. Must be 6 digits.")
        return

    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    try:
        class_standing = float(input("Class Standing (0-100): "))
        major_exam = float(input("Major Exam (0-100): "))
        if not (0 <= class_standing <= 100 and 0 <= major_exam <= 100):
            raise ValueError("Grades must be between 0 and 100.")
    except ValueError as e:
        print("Invalid input:", e)
        return

    records.append(Student(student_id, first_name, last_name, class_standing, major_exam))
    print("Record added successfully.")

def edit_record(records):
    student_id = input("Enter Student ID to edit: ")
    for i, record in enumerate(records):
        if record.student_id == student_id:
            first_name = input(f"New First Name ({record.first_name}): ").strip() or record.first_name
            last_name = input(f"New Last Name ({record.last_name}): ").strip() or record.last_name
            try:
                class_standing = float(input(f"New Class Standing ({record.class_standing}): ") or record.class_standing)
                major_exam = float(input(f"New Major Exam ({record.major_exam}): ") or record.major_exam)
            except ValueError:
                print("Invalid input. Keeping previous values.")
                return
            records[i] = Student(student_id, first_name, last_name, class_standing, major_exam)
            print("Record updated.")
            return
    print("Record not found.")

def delete_record(records):
    student_id = input("Enter Student ID to delete: ")
    for i, record in enumerate(records):
        if record.student_id == student_id:
            del records[i]
            print("Record deleted.")
            return
    print("Record not found.")

def show_student_record(records):
    student_id = input("Enter Student ID: ")
    for record in records:
        if record.student_id == student_id:
            print(f"ID: {record.student_id}, Name: {record.first_name} {record.last_name}, Final Grade: {record.final_grade():.2f}")
            return
    print("Record not found.")

def main():
    filename = "students.txt"
    records = load_records(filename)
    
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            filename = input("Enter filename to open: ")
            records = load_records(filename)
            print("File opened.")
        elif choice == '2':
            save_records(records, filename)
        elif choice == '3':
            save_as_file(records)
        elif choice == '4':
            display_records(records)
        elif choice == '5':
            display_records(records, "last_name")
        elif choice == '6':
            display_records(records, "grade")
        elif choice == '7':
            show_student_record(records)
        elif choice == '8':
            add_record(records)
        elif choice == '9':
            edit_record(records)
        elif choice == '10':
            delete_record(records)
        elif choice == '11':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
