#!/usr/bin/python3
"""first api module"""
import json
import requests

if __name__ == "__main__":
    res = requests.get("https://jsonplaceholder.typicode.com/users").json()
    user_todo = {}
    i = 1
    for user in res:
        with requests.get(
            f"https://jsonplaceholder.typicode.com/users/{i}/todos"
        ) as json_response:
            todos = json.loads(json_response.content)
            employee_name = user.get("username")
        for todo in todos:
            todo["username"] = employee_name
            todo["task"] = todo.get("title")
            todo.pop("id")
            todo.pop("title")
            todo.pop("userId")
        user_todo[f"{i}"] = todos
        i += 1
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_todo, json_file)
