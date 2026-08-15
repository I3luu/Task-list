from TaskList import TaskList

def test_add_task():
    my_list = TaskList()
    my_list.add_task("buy milk")
    assert my_list.tasks[0].title == "buy milk"

def test_complete_task():
    my_list = TaskList()
    my_list.add_task("buy milk")
    my_list.add_task("learn python")
    my_list.complete_task(1)
    assert my_list.tasks[1].done == True

def test_delete_task():
    my_list = TaskList()
    my_list.add_task("buy milk")
    my_list.add_task("learn python")
    my_list.delete_task(0)
    assert len(my_list.tasks) == 1
    assert my_list.tasks[0].title == "learn python"

def test_save_and_load():
    my_list = TaskList()
    my_list.add_task("buy milk")
    my_list.add_task("learn python")
    my_list.save_to_file("test_tasks.json")

    new_list = TaskList()
    new_list.load_from_file("test_tasks.json")

    assert new_list.tasks[0].title == "buy milk"
    assert new_list.tasks[0].done == False   
