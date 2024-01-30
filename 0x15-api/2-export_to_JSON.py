#!/usr/bin/python3
"""first api module"""
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
        employee_name = user_dict.get("username")
    for todo in todos:
        todo["username"] = employee_name
        todo["task"] = todo.get("title")
        todo.pop("id")
        todo.pop("title")
        todo.pop("userId")
    user_todo = {}
    user_todo[argv[1]] = todos
    with open(f"{argv[1]}.json", "w") as json_file:
        json.dump(user_todo, json_file)
