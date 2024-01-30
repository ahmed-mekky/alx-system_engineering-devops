#!/usr/bin/python3
"""first api module"""
import csv
import json
import requests
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
    for todo in todos:
        todo["name"] = employee_name
        todo.pop("id")
    user_id = todos[0].get("userId")
    f = ["userId", "name", "completed", "title"]  # fiels names
    with open(f"{user_id}.csv", "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, quoting=csv.QUOTE_ALL, fieldnames=f)
        writer.writerows(todos)
