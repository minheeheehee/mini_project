from flask import Flask, render_template
from todo1_view import todo01
from todo2_view import todo02
from todo3_view import todo03

app = Flask(__name__)

app.register_blueprint(todo01)
app.register_blueprint(todo02)
app.register_blueprint(todo03)

@app.route('/')
def index():
    return render_template('index.html')

