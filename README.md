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



