# Personal Daily Reminder Application
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} requires moderate attention, should be completed the next 3 days!")
        else:
            print(f"Reminder: {task} is a medium priority task. Try to complete it when you can.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task but has a deadline. Try to complete it within the week.")
        else:
            print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("You can rest or have some fun.")