import csv  # To read the currency data from the CSV file

# Dictionary to store exchange rates
exchange_rates = {}

# Read the CSV file and store exchange rates
try:
    with open("currency.csv", mode="r", encoding="utf-8", errors="replace") as file:
        reader = csv.reader(file)  # Create a reader object
        next(reader)  # Skip the header row

        for row in reader:
            if len(row) < 3:  # Ensure the row has at least 3 columns (code, name, rate)
                continue

            code = row[0].strip()  # Currency code

            try:
                rate = float(row[2].strip())  # Convert the exchange rate to a floating-point number 
                exchange_rates[code] = rate  # Store the exchange rate in the dictionary
            except ValueError:
                continue

except FileNotFoundError:
    print("Error: currency.csv file not found!")
    exit()

# Get user input
try:
    dollar_amount = float(input("\nHow much dollar do you have? "))  # Ask for dollar input
    target_currency = input("What currency do you want to have? ").strip().upper()  # Ask for target currency 

    if target_currency in exchange_rates:  # Check if the entered currency code exists 
        converted_amount = dollar_amount * exchange_rates[target_currency]  # Perform the conversion

        # Display the results
        print(f"\nDollar: {int(dollar_amount)} USD")
        print(f"{target_currency}: {converted_amount:.9f}")  # 9 decimal places
    else:
        print("Invalid currency code. Please try again.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
