# Accept input for student details
last_name = input("Enter Last Name: ").strip()
first_name = input("Enter First Name: ").strip()
age = input("Enter Age: ").strip()
contact_number = input("Enter Contact Number: ").strip()
course = input("Enter Course: ").strip()

# Create a formatted string with student details
student_info = f"""
Last Name: {last_name}
First Name: {first_name}
Age: {age}
Contact Number: {contact_number}
Course: {course}
-----------------------------
"""

# Student info to the file using 'with open()' for better file handling
file_path = "C:\\Users\\Cheetos\\Documents\\Practice Coding\\Activity 03\\Student.txt"

try:
    with open(file_path, "a") as file:
        file.write(student_info)
    print("\nStudent information has been successfully saved to 'students.txt'.")
except Exception as e:
    print(f"\nError saving student information: {e}")
