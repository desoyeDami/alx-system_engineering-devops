#!/usr/bin/python3
# Python script to export employee TODO list data to a CSV file
import requests
import csv
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetch the TODO list of an employee and export it to a CSV file.
    
    Args:
        employee_id (int): The ID of the employee.
    
    Returns:
        None
    """
    GENERAL_URL = "https://jsonplaceholder.typicode.com/"
    
    # Fetch employee details
    EMPLOYEE_URL = f"{GENERAL_URL}/users/{employee_id}"
    employee_response = requests.get(EMPLOYEE_URL).json()
    employee_name = employee_response.get('username')

    # Fetch employee's TODO list
    TODO_URL = f"{GENERAL_URL}/todos?userId={employee_id}"
    todos = requests.get(TODO_URL).json()

    # Export data to CSV
    export_to_csv(employee_id, employee_name, todos)

def export_to_csv(employee_id, employee_name, todos):
    """
    Export employee TODO list to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The name of the employee.
        todos (list): The list of TODO tasks.

    Returns:
        None
    """
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write each task's data to the CSV
        for todo in todos:
            writer.writerow([
                f'"{employee_id}"',
                f'"{employee_name}"',
                f'"{todo.get("completed")}"',
                f'"{todo.get("title")}"'
            ])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py EMPLOYEE_ID")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")

