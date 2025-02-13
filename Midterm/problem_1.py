def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    try:
        with open(filename) as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    numbers = list(map(int, line.strip().split(',')))
                    total = sum(numbers)
                    status = "Palindrome" if is_palindrome(total) else "Not a palindrome"
                    formatted_numbers = ", ".join(map(str, numbers))
                    print(f"Line {line_number}: {formatted_numbers} (sum {total}) - {status}")
                except ValueError:
                    print(f"Line {line_number}: Invalid data format (skipped)")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

process_file("numbers.txt")
