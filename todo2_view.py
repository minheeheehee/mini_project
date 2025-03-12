from flask import Flask, render_template

todo02 = Flask(__name__)

todos = [{'tno':1, 'title':'전투체육', 'date':'2025-03-12'},
         {'tno':2, 'title':'미용실방문', 'date':'2025-03-12'}]
@todo02.route("/todo2/list")
def list():
    count = len(todos)
    return render_template("todo2/list.html", todos=todos, count=count)


todo02.run(debug=True)