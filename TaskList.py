class Task:
    def __init__(self, title):
        self.title = title
        self.done = False




class TaskList:
    def __init__(self):
        self.tasks = []
    def add_task(self,title):
        new_task = Task(title)
        self.tasks.append(new_task)
    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            print(i, task.title, task.done)
    def complete_task(self, index):
        self.tasks[index].done = True
        

my_list = TaskList()
my_list.add_task("buy milk")
my_list.add_task("walk dog")
my_list.complete_task(0)
my_list.show_tasks()
