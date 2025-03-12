from flask import Flask,Blueprint, render_template

todo02 = Blueprint('todo2',__name__, url_prefix='/todo2')

todos = [{'tno':1, 'title':'전투체육', 'date':'2025-03-12'},
         {'tno':2, 'title':'미용실방문', 'date':'2025-03-12'}]

@todo02.route("/list")
def list():
    count = len(todos)
    return render_template("todo2/list.html", todos=todos, count=count)

