from flask import Flask,request,render_template,session
from flask_session import Session
app=Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

notes = []
@app.route('/', methods=['GET', 'POST','PUT','PATCH','DELETE'])
def event():
    if request.method == 'POST':
        note = request.form.get('note')
        notes.append(note)
def delete():
    if request.method == 'DELETE':
        note = request.form.get('note')
        note.remove(note)
# i think im going to use this method, or i was thinking combining delete and post
def modify():
    if request.method == 'PATCH':
        note = request.form.get(note)
            for note in notes
            note.patch(notes)
# need to include a class system or mocking?

    return render_template("home.html", notes=notes)
