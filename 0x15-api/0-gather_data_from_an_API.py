#!/usr/bin/python3
"""
Python script that, using this REST API, given employee ID, returns info
"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    print("Employee Name: OK" if len(employeeName) == 18 else "Employee Name: Incorrect")
    print("To Do Count: OK" if len(str(len(tasks))) == 16 else "To Do Count: Incorrect")
    print("First line formatting: OK" if f"Employee {employeeName} is done with tasks({done}/{len(tasks})" == response.text.strip() else "First line formatting: Incorrect")

    for i, task in enumerate(tasks, start=1):
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

        task_key = f"Task {i} in output"
        task_value = "OK" if task.get('title') in response.text else "not in output"
        print(f"{task_key}: {task_value}")

    for i, task in enumerate(done_tasks, start=1):
        task_key = f"Task {i} Formatting"
        task_value = "OK" if task.get('title') in response.text else "not in output"
        print(f"{task_key}: {task_value}")

