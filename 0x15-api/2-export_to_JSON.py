#!/usr/bin/python3
"""
Writes information about his/her TODO list progress
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress
    of a given employee from a REST API.

    Parameters:
        employee_id (int): The unique ID of the employee whose TODO
                           progress is to be fetched.

    Returns:
        None: This function displays the employee's TODO lis
                progress on the standard output.

    Raises:
        ValueError: If the provided employee_id is not an integer.

    """

    # Replace this with the actual API URL
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, sys.argv[1])
    todos_url = "{}/todos/".format(user_url)

    # Extract relevant information from the response
    employee = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    # Extract the employee name
    employee_name = employee["name"]

    completed_tasks = [task for task in todos if task["completed"]]
    len_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)

    # Display the information in the specified format
    first_line = "Employee {} is done with tasks({}/{}):"\
                 .format(employee_name, len_completed_tasks, total_tasks)

    # Print the first_line
    # print(first_line)

    # Display the titles of completed tasks
    filename = "{}.json".format(employee_id)

    # open new file for writing - will erase file if it already exists
    with open(filename, mode="w", newline='') as jsonfile:

        tasks_dict = {str(employee_id): []}

        for task in todos:
            employee_id = task["userId"]
            employee_username = employee["username"]
            task_completed_status = task["completed"]
            task_title = task["title"]

            task_dict = {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee["username"]
                }

            tasks_dict[str(employee_id)].append(task_dict)

            # print(res)
            json.dump(tasks_dict, jsonfile)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please enter an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
