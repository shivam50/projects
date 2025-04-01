import json

print("Welcome Traveller! What would you like to do?")
ops = input("Add/Update/Delete Task: ")

with open('taskspy.json', 'r') as file:
    tasks = json.load(file)

if ops == "Add":
    tasks.append({"task": input("Task: "), "date": input("Date: "), "time": input("Time: ")})
    print("Task added.")
    with open('taskspy.json', 'w') as file:
        json.dump(tasks, file)

elif ops == "Update":
    task_to_update = input("Task to update: ")
    for task in tasks:
        if task["task"] == task_to_update:
            task.update({"task": input("New Task: "), "date": input("New Date: "), "time": input("New Time: ")})
            print("Task updated.")
            break
    else:
        print("Task not found.")

elif ops == "Delete":
    tasks = [task for task in tasks if task["task"] != input("Task to delete: ")]
    print("Task deleted.")

else:
    print("Invalid operation.")

with open('taskspy.json', 'w') as file:
    json.dump(tasks, file)
