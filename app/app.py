from flask import Flask, request, render_template,url_for,redirect
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/alanchery/Desktop/Project1/app/todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.session.delete

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('different.html', todos=todos)

@app.route('/plus', methods=['POST'])
def add():
        todos = Todo(text=request.form['todoitem'], complete=False)
        db.session.add(todos)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST','GET'])
def delete(todo_id):
#checking if the todo is there
    if todo is None:
        redirect(url_for('index'))
# looking up id to delete by the user ID
    todo_id = Todo.query.filter_by(todo_id=todo_id).delete()
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
