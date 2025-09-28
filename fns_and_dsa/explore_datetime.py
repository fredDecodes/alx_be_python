# Datetime module exploration
from datetime import datetime, timedelta

current_datetime = datetime.now()

def display_current_datetime():
    # Get the current date and time
    current_date = current_datetime.date().strftime("%Y-%m-%d")
    current_time = current_datetime.time().strftime("%H:%M:%S")
    print(f"Current date and time: {current_date} {current_time}")

def calculate_future_date():
    # Calculate a future date by adding days
    days_ahead = int(input("Enter number of days to add: "))
    future_date = current_datetime.date() + timedelta(days=days_ahead)
    print(f"Future date: {future_date}")

display_current_datetime()
calculate_future_date()
