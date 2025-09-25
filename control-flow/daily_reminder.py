# Personal Daily Reminder Application
task = input("Enter the task you want to be reminded of daily: ")
task_priority = input("Enter the priority level (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

match (task_priority):
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
            print(f"Reminder: {task} is on the low but time bound, maximum 5 days to complete.")
        else:
            print("Consider completing it when you have free time.")
    case _:
        print("You can rest or have some fun.")