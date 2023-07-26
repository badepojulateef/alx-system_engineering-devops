#!/usr/bin/python3
"""
Returns information about his/her TODO list progress
"""

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
    base_url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(base_url + "todos", params={"userId": sys.argv[1]})\
                    .json()

    # print(users)
    # print('-------------')
    # print(todos)
    # Fetch the employee's TODO list progress from the API

    # data = users.json()

    # Extract relevant information from the response
    employee_name = users["name"]
    done_tasks = [task for task in todos if task["completed"]]
    num_done_tasks = len(done_tasks)
    total_tasks = len(todos)

    # Display the information in the specified format
    output = "Employee {} is done with tasks({}/{}):"\
             .format(employee_name, num_done_tasks, total_tasks)

    print(output)

    # Display the titles of completed tasks
    for task in done_tasks:
        print("\t{}".format(task['title']))


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
