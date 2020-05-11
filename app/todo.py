from flask import Flask,request,render_template,session
from flask_session import Session

app=Flask(__name__)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"

notes = []
# using counter to add ID's
counter = 0
@app.route('/post', methods=['POST'])
def event():
    if request.method == 'POST':
        note = request.form.get('note')
        new_note = {
            'id':counter,
            'todo':note
        }
        up()
        notes.append(new_note)
    return render_template("home.html", notes=notes)

@app.route('/', methods=['GET'])
def find():
    if request.method == 'GET':
        note = request.form.get('note')

    return render_template("home.html", notes=notes)

@app.route('/delete', methods=['POST'])
def delete():
        for note in notes:
            if id == request.form.get(id):
                notes.remove(note)

        return render_template("home.html", notes=notes)

def up():
    global counter
    counter += 1

if __name__ == "__main__":
    app.run()
