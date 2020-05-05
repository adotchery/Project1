from flask import Flask,request,render_template,session
from flask_session import Session
app=Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

notes = []
@app.route('/', methods=['GET', 'POST'])
def event():
    if request.method == 'POST':
        note = request.form.get('note')
        notes.append(note)

    return render_template("home.html", notes=notes)
