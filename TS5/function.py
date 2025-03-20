def divide(x, y):
    if y != 0:
        return x / y
    else:
        return None

def exponentiate(x, y):
    return x ** y

def remainder(x, y):
    if y != 0:
        return x % y
    else:
        return None

def summation(x, y):
    if y >= x:
        return sum(range(x, y + 1))
    else:
        return None

def main():
    while True:
        print("\n--- Menu ---")
        print("[D] Divide")
        print("[E] Exponentiation")
        print("[R] Remainder")
        print("[F] Summation")
        print("[Q] Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'Q':
            print("Exiting program...")
            break

        if choice not in ['D', 'E', 'R', 'F']:
            print("Invalid choice! Please enter a valid option.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        result = None

        if choice == 'D':
            result = divide(num1, num2)
            if result is None:
                print("Error: Cannot divide by zero!")
            else:
                print(f"Result of division: {result}")

        elif choice == 'E':
            result = exponentiate(num1, num2)
            print(f"Result of exponentiation: {result}")

        elif choice == 'R':
            result = remainder(num1, num2)
            if result is None:
                print("Error: Cannot find remainder when divisor is zero!")
            else:
                print(f"Remainder: {result}")

        elif choice == 'F':
            result = summation(num1, num2)
            if result is None:
                print("Error: Second number must be greater than or equal to the first number for summation!")
            else:
                print(f"Summation result: {result}")

if __name__ == "__main__":
    main()
