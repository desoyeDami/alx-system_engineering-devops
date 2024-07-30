#!/usr/bin/python3
"""
    Python script that returns an employee todo
    info by taking the employee's id
"""
import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Function to  Get employee todo progress """
    GENERAL_URL = "https://jsonplaceholder.typicode.com/"

    # Employee Deta
    EMPLOYEE_URL = f"{GENERAL_URL}/users/{employee_id}"
    EMPLOYEE_RESPONSE = requests.get(EMPLOYEE_URL).json()
    EMPLOYEE_NAME = EMPLOYEE_RESPONSE.get('name')

    # Employee Todo list
    TODO_URL = f"{GENERAL_URL}/todos?userId={employee_id}"
    TODOs = requests.get(TODO_URL).json()

    # Completed task
    TASKS_COMPLETED = [todo for todo in TODOs if todo.get('completed')]
    TOTAL_NUMBER_OF_TASKS = len(TODOs)
    NUMBER_OF_DONE_TASKS = len(TASKS_COMPLETED)

    # Export
    export_csv(employee_id, EMPLOYEE_NAME, TODOs)


def export_csv(employee_id, EMPLOYEE_NAME, TODOs):
    """ FUnction to create a csv file and input task details"""
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        w = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in TODOs:
            w.writerow([
                f"{employee_id}",
                f"{EMPLOYEE_NAME}",
                f"{todo.get('completed')}",
                f'{todo.get("title")}'
                ])


if __name__ == "__main__":
    """To Prevent code from executing when imported"""
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
