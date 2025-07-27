
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date)

def calculate_future_date():
    days = int(input("Enter number of days to add: "))
    future_date = datetime.now() + timedelta(days=days)
    print("Future date:", future_date.date())

display_current_datetime()
calculate_future_date()
