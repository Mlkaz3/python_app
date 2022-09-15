from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "Winnie"
    age = 22
    occupation = "Programmer | Data Lab Research Assistant "
    return render_template('index.html', name=name, age=age, occupation=occupation)