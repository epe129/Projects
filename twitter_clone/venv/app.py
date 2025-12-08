from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():

    return render_template("/pages/login.html")

@app.route('/register', methods =["GET", "POST"])
def register():
    username = ""
    password = ""
    passwordConfirm = ""
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("pwd") 
       
        passwordConfirm = request.form.get("pwdConfirm")
       
        new_employee = {
            "username": f"{username}",
            "password": f"{password}",
        }
       
        if password == passwordConfirm:
            return
       
       
        username = ""
        password = ""
        passwordConfirm = ""
    

    return render_template("/pages/register.html")


if __name__ == '__main__':
    app.run()