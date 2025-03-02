# Get user input for first and last name
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Concatenate the first and last name into a full name
full_name = f"{first_name} {last_name}"

# Display full name
print("\nFull Name:", full_name)

# Display full name in uppercase
print("Full Name (Uppercase):", full_name.upper())

# Display full name in lowercase
print("Full Name (Lowercase):", full_name.lower())

# Count and display the length of the full name (excluding spaces)
name_length = len(full_name.replace(" ", ""))
print("Full Name Length (without spaces):", name_length)
