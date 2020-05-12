from flask import Flask, request, render_template,url_for,redirect
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/alanchery/Desktop/Project1/app/todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.session.delete

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('different.html', users=users)

@app.route('/plus', methods=['POST'])
def add():
        user = User(text=request.form['todoitem'], complete=False)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/delete', methods=['POST','GET'])
def delete():
    user = User.query.get(1)
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('delete'))

if __name__ == "__main__":
    app.run()
