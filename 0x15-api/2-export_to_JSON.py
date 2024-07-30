#!/usr/bin/python3
"""
    Python script that returns an employee todo
    info by taking the employee's id
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Function to  Get employee todo progress """
    GENERAL_URL = "https://jsonplaceholder.typicode.com/"

    # Employee Deta
    EMPLOYEE_URL = f"{GENERAL_URL}/users/{employee_id}"
    EMPLOYEE_RESPONSE = requests.get(EMPLOYEE_URL).json()
    EMPLOYEE_NAME = EMPLOYEE_RESPONSE.get('username')

    # Employee Todo list
    TODO_URL = f"{GENERAL_URL}/todos?userId={employee_id}"
    TODOs = requests.get(TODO_URL).json()

    # Completed task
    TASKS_COMPLETED = [todo for todo in TODOs if todo.get('completed')]

    # Export
    export_json(employee_id, EMPLOYEE_NAME, TODOs)


def export_json(employee_id, EMPLOYEE_NAME, TODOs):
    """ FUnction to create a json file and input task details"""
    data = {
        employee_id: [
            {
                "task": todo.get("title"),
                "completed": todo.get('completed'),
                "username": EMPLOYEE_NAME
            }
            for todo in TODOs
            ]
    }

    filename = f"{employee_id}.json"
    with open(filename, mode='w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    """To Prevent code from executing when imported"""
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
