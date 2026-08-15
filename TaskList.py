import json




class Task:
    def __init__(self, title):
        self.title = title
        self.done = False


class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            print(i, task.title, task.done)

    def complete_task(self, index):
        self.tasks[index].done = True

    def delete_task(self, index):
        self.tasks.pop(index)

    def save_to_file(self, filename):
        data = [{"title": task.title, "done": task.done} for task in self.tasks]
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)

        for item in data:
            new_task = Task(item["title"])
            new_task.done = item["done"]
            self.tasks.append(new_task)


my_list = TaskList()
my_list.add_task("buy milk")
my_list.add_task("walk dog")
my_list.save_to_file("tasks.json")

new_list = TaskList()
new_list.load_from_file("tasks.json")
new_list.show_tasks()

