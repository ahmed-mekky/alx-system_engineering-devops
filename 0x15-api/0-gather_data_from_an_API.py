#!/usr/bin/python3
"""first api module"""
import requests
import json
from sys import argv

if __name__ == "__main__":

    with requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    ) as json_response:
        todos = json.loads(json_response.content)
        with requests.get(
            f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
        ) as json_user:
            user_dict = json.loads(json_user.content)
            employee_name = user_dict.get("name")
        completed_tasks, total_tasks = 0, 0
        tasks = []
        for todo in todos:
            if todo.get("completed") is True:
                completed_tasks += 1
                tasks.append(todo.get("title"))
            total_tasks += 1
        print(
            f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):"
        )
        for task in tasks:
            print(f"     {task}")
