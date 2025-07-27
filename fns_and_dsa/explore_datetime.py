from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)


def calculate_future_date():
    days_input = input("Enter the number of days to add to the current date: ")

    if days_input.isdigit():
        days = int(days_input)
        future_date = datetime.now() + timedelta(days=days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print("Future date:", formatted_future)
    else:
        print("Invalid input. Please enter a number.")

display_current_datetime()
calculate_future_date()