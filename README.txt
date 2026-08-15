TASK LIST

A simple command-line to-do list app built in Python, using object-oriented programming to manage tasks with persistent storage.


FEATURES

add tasks

mark them as complete

delete tasks

view all tasks + completion status

save and load data between runs

covered by pytest


REQUIREMENTS

Python 3

Pytest




INSTALL PYTEST:

pip install pytest



RUN DIRECTLY WITH:
python tasklist.py



HOW IT WORKS:
Task is a single task, with a title and done status.

TaskList manages a collection of task objects and has methods to add, delete, complete, display, save, and load tasks.

Tasks are saved to and loaded from a JSON file, changing them from task objects to dictionaries to get around JSON not being able to store custom objects in python directly.



ROADMAP:

Web interface

Due dates and priorities

CLI support for quick actions



