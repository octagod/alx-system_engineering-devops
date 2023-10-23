#!/usr/bin/python3
""" module doc """
import sys
import requests


def main():
    """ def com """
    id = sys.argv[1]
    print(id)
    url = 'https://jsonplaceholder.typicode.com/'
    users = f'users/{id}'
    todos = f'todos?userId={id}'
    user_data = requests.get(f'{url}{users}', timeout=10).json()
    name = user_data.get("name")
    todos_data = requests.get(f'{url}{todos}', timeout=15).json()
    # get number of completed task from todo data
    completed = filter(is_complete, list(todos_data))
    total_todo = len(todos_data)
    done_todos = list(completed)
    print(f'Employee {name} is done with tasks({len(done_todos)}/{total_todo}):')
    for task in done_todos:
        print("\t "+task.get("title"))


def is_complete(todo):
    """Check if todo is complete"""
    return todo["completed"]


if __name__ == "__main__":
    main()
