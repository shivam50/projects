#!/bin/bash

# Ensure the JSON file exists
if [[ ! -f tasks.json ]]; then
    echo "[]" > tasks.json
fi

echo "Hello Traveller, what do you want to do today?"
echo "1. Add Task"
echo "2. Delete Task"
echo "3. Update Task"
read -p "Choose an option (1/2/3): " OPS

case $OPS in 
    1 | "Add" | "Add Task")
        read -p "Input Task: " task
        read -p "Input Date (YYYY-MM-DD): " date
        read -p "Input Time (HH:MM): " time
        
        jq --arg task "$task" --arg date "$date" --arg time "$time" \
           '. + [{"task": $task, "date": $date, "time": $time}]' tasks.json > temp.json && mv temp.json tasks.json
        echo "Task added successfully."
        ;;
    2 | "Delete" | "Delete Task")
        # Delete Task
        read -p "Enter Task name to delete: " task
        
        # Deleting the task from JSON
        jq --arg task "$task" 'map(select(.task != $task))' tasks.json > temp.json && mv temp.json tasks.json
        echo "Task deleted successfully."
        ;;
    3 | "Update" | "Update Task")
        # Update Task
        read -p "Enter Task name to update: " task
        read -p "Enter new Date (YYYY-MM-DD): " new_date
        read -p "Enter new Time (HH:MM): " new_time
        
        # Update the task in JSON
        jq --arg task "$task" --arg new_date "$new_date" --arg new_time "$new_time" \
           'map(if .task == $task then .date = $new_date | .time = $new_time else . end)' tasks.json > temp.json && mv temp.json tasks.json
        echo "Task updated successfully."
        ;;
    *)
        echo "Invalid option, please try again."
        ;;
esac
