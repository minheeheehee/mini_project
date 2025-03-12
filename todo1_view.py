from flask import Flask, render_template 

todo1 = Flask(__name__)

todos=[{'tno':1, 'title':'전투체육','date':'2025-03-12'},
 {'tno':2, 'title':'미용실 방문','date':'2025-03-12'}
 ]
@todo1.route("/todo1/list")
def list():
	count= len(todos)
	return render_template("todo1/list.html",todos=todos, count=count)




todo1.run(debug=True)