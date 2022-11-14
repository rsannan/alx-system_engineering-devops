#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    employee_req = requests.get('{}users'.format(url))
    employee_list = employee_req.json()
    todo_list = requests.get('{}todos'.format(url))
    all_todos = todo_list.json()

    for item in employee_list:
        username = item.get('username')
        eid = item.get('id')
        user_todo = []
        for item in all_todos:
            if item.get('userId') == int(eid):
                user_todo.append(item)
        with open('todo_all_employees.json', 'a', encoding='UTF8') as f:
            row = list(map(
                           lambda x: {
                                     "task": x.get("title"),
                                     "completed": x.get("completed"),
                                     "username": username
                                      }, user_todo))
            json_data = {"{}".format(eid): row}
            json.dump(json_data, f)
