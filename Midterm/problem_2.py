from datetime import datetime

def format_date():
    str_date = input("Enter date (mm/dd/yyyy): ")
    try:
        month, day, year = map(int, str_date.split('/'))
        date_obj = datetime(year, month, day)
        print(f"Formatted Date: {date_obj:%B %d, %Y}")
    except ValueError:
        print("Invalid date format. Please enter in mm/dd/yyyy format.")

format_date()
