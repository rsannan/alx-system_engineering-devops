#!/usr/bin/python3
"""
for a given employee ID, returns information about his/her TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    eid = sys.argv[1]
    employee_req = requests.get('{}users/{}'.format(url, eid))
    employee_list = employee_req.json()
    employee_name = employee_list.get('name')
    todo_list = requests.get('{}todos'.format(url))
    all_todos = todo_list.json()
    todo = 0
    done = 0
    for item in all_todos:
        if item.get('userId') == int(eid):
            todo += 1
            if item.get('completed') is True:
                done += 1
    print('Employee {} is done with tasks({}/{}):'.format(
                                                  employee_name,
                                                  done, todo))

    for item in all_todos:
        if item.get('userId') == int(eid) and item.get('completed') is True:
            print('\t {}'.format(item.get('title')))
