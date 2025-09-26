# Personal Daily Reminder Application
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match (priority):
    case "high":
        if (time_bound == "yes"):
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print("Requires immediate attention.")
    case "medium":
        if (time_bound == "yes"):
            print(f"Reminder: {task} requires moderate attention, should be completed the next 2 days!")
        else:
            print("Maximum 3 days, get it done.")
    case "low":
        if (time_bound == "yes"):
            print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print("Consider doing it whenever possible.")
    case _:
        print("You can rest or have some fun.")