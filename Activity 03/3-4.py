file_path = "C:\\Users\\Cheetos\\Documents\\Practice Coding\\Activity 03\\Student.txt"

try:
    # Open the file in read mode using 'with' to ensure proper handling
    with open(file_path, "r") as file:
        student_info = file.read().strip()  # Read and remove leading/trailing whitespace

    if student_info:
        print("\nReading Student Information:")
        print(student_info)
    else:
        print("No student information found in 'students.txt'.")

except FileNotFoundError:
    print("Error: 'students.txt' not found.")
except PermissionError:
    print("Error: You don't have permission to access 'students.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
