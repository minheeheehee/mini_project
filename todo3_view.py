from flask import Flask,render_template

todo03 = Flask(__name__)

todos=[{'tno':1, 'title':'전투체육', 'date':'2050-03-12'},
       {'tno':2, 'title':'미용실방문', 'date':'2050-03-12'}]
@todo03.route('/todo3/list')
def list():
    count=len(todos)
    return render_template('todo3/list.html', todos=todos, count=count)






todo03.run(debug=True)