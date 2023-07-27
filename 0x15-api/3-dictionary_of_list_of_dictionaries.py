#!/usr/bin/python3
"""
Records all tasks from all employees
"""

import json
import requests
import sys


def get_all_employee_todo_progress():
    """
    Retrieves and displays the TODO list progress
    of a given employee from a REST API.

    Parameters:

    Returns:
        None: This function displays the employee's TODO lis
                progress on the standard output.

    Raises:
        ValueError: If the provided script is not an integer.

    """

    # Replace this with the actual API URL
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users".format(base_url)

    employees = requests.get(users_url).json()

    tasks_dict = {}

    for employee in employees:
        # print(employee)
        # print("---------")
        employee_id = employee['id']
        # print("---------")
        todos_url = "{}/{}/todos".format(users_url, employee['id'])
        # print(todos_url)
        employee_todos = requests.get(todos_url).json()

        tasks_dict[employee_id] = []

        for task in employee_todos:
            tasks_dict[employee_id].append({
                "task": task["title"],
                "completed": task["completed"],
                "username": employee["username"]
            })

        # print(tasks_dict)

    # open new file for writing - will erase file if it already exists
    with open(str("todo_all_employees.json"), mode="w", newline='') as file:
        json.dump(tasks_dict, file)


if __name__ == "__main__":
    """ Records all tasks from all employees """
    if len(sys.argv) != 1:
        print("Usage: python script.py")
        sys.exit(1)

    get_all_employee_todo_progress()
