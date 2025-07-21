task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()

while True:
    time = input("Time bound? (yes/no)").lower()
    if time == "yes" or time == "y" or time == "no" or time == "n":
        break
    else:
        print("Invalid input, please try again")
        

            
match priority:
       
        case "high":
            if time == "yes" or "y":
                print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
            else:
                print(f"Note: {task} is pending, don't forget!")
        case "medium":
            if time == "yes" or "y":
                print(f"{task} is a {priority} priority task and must be done soon!")
            else:
                print(f"Note: {task} is pending, work on it when possible!")
        case "low":
            if time == "yes" or "y":
                print(f"Gentle Reminder: {task} is a {priority} priority task. Keep in mind!")
            else:
                print(f"Note! {task} is a {priority} task. Consider completing it when you have free time.")