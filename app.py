from flask import Flask, render_template, request, redirect
from TaskList import TaskList


app = Flask(__name__)
my_list = TaskList()

try:
    my_list.load_from_file("tasks.json")
except FileNotFoundError:
    pass

@app.route("/")
def index():
    return render_template("index.html", tasks=my_list.tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    my_list.add_task(title)
    my_list.save_to_file("tasks.json")
    return redirect("/")

@app.route("/complete/<int:index>", methods=["POST"])
def complete(index):
    my_list.complete_task(index)
    my_list.save_to_file("tasks.json")
    return redirect("/")

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    my_list.delete_task(index)
    my_list.save_to_file("tasks.json")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


 