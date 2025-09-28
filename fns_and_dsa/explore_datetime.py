# Datetime module exploration
from datetime import datetime, timedelta

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def display_current_datetime():
    # Get the current date and time
    current_date = current_datetime.date()
    current_time = current_datetime.time()
    print(f"Current date and time: {current_date} {current_time}")

def calculate_future_date():
    # Calculate a future date by adding days
    days_ahead = int(input("Enter the number of days to add to the current date: "))
    future_date = current_datetime.date() + timedelta(days=days_ahead)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

display_current_datetime()
calculate_future_date()
