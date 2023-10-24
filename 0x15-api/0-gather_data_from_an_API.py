#!/usr/bin/python3
""" module doc """
import requests
import sys


def main():
    """ def com """
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    users = f'users/{id}'
    todos = f'todos?userId={id}'
    user_data = requests.get(f'{url}{users}', timeout=10).json()
    name = user_data.get("name")
    todos_data = requests.get(f'{url}{todos}', timeout=15).json()
    completed = filter(is_complete, list(todos_data))
    total = len(todos_data)
    done_t = list(completed)
    print(f'Employee {name} is done with tasks({len(done_t)}/{total}):')
    for task in done_t:
        print("\t "+task.get("title"))


def is_complete(todo):
    """Check if todo is complete"""
    return todo.get("completed")


if __name__ == "__main__":
    main()
