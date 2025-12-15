from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import json
import sqlite3

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False     
app.config["SESSION_TYPE"] = "filesystem"     

Session(app)

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/page', methods =["GET", "POST"])
def page():
    username = ""
    tweet = ""
    user = ""
    PrivateOrPublic = ""
    data = []

    conn = sqlite3.connect('/home/lenni/home/koodit/projects/twitter_clone/venv/db/tweets.db')

    c = conn.cursor()

    if not session.get("username"):
        return redirect("/login")
    else:
        username = session.get("username")
    
    if request.method == "POST":
        tweet = request.form.get("tweet")
        user = session.get("username")
        PrivateOrPublic = request.form.getlist('checkbox')
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS tweets (
                USERNAME TEXT NOT NULL,
                STATUS TEXT NOT NULL,
                TWEET TEXT NOT NULL
            )
        ''')

        c.execute(f"INSERT INTO tweets (USERNAME, STATUS, TWEET) VALUES ('{user}', '{PrivateOrPublic[0]}', '{tweet}')")

        conn.commit()
        
        
    tweet = ""
    user = ""
    PrivateOrPublic = ""
    
    c.execute("SELECT * FROM tweets")

    rows = c.fetchall()

    for c in rows:
        if c[1] == "Private":
            continue
        elif c[1] == "Public":
            data.append(c)
    
    print(data)

    p = len(data)


    return render_template("/pages/Thepage.html", username=username, data=data, p=p)


@app.route('/login', methods =["GET", "POST"])
def login():
    conn = sqlite3.connect('/home/lenni/home/koodit/projects/twitter_clone/venv/db/users.db')

    c = conn.cursor()

    c.execute("SELECT * FROM users")

    rows = c.fetchall()
    
    if request.method == "POST":
        username = request.form.get("username")
        session["username"] = username
        password = request.form.get("pwd") 
        NotExist = "User not exist"
       
        for rivi in rows:
            if username == rivi[0] and password == rivi[1]:
                return redirect("page")
            else:
                return render_template("/pages/login.html", NotExist=NotExist)                
    
        c.close()

    return render_template("/pages/login.html")

@app.route('/register', methods =["GET", "POST"])
def register():
    username = ""
    password = ""
    passwordConfirm = ""

    SameUsername = "Username is taken"
    PasswordMatch = "Password not maching"
    empty = "Username or password field is empty"
        
    conn = sqlite3.connect('/home/lenni/home/koodit/projects/twitter_clone/venv/db/users.db')

    c = conn.cursor()

    if request.method == "POST":
        username = request.form.get("username")
        session["username"] = username
        password = request.form.get("pwd") 
       
        passwordConfirm = request.form.get("pwdConfirm")
          
        if password != passwordConfirm:
            return render_template("/pages/register.html", PasswordMatch=PasswordMatch)            
        
        if username == "" or password == "":
            return render_template("/pages/register.html", empty=empty)
                    
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                USERNAME TEXT NOT NULL,
                PASSWORD TEXT NOT NULL
            )
        ''')

        c.execute("SELECT * FROM users")

        rows = c.fetchall()

        for rivi in rows:
            if username == rivi[0]:
                return render_template("/pages/register.html", SameUsername=SameUsername)
       
        c.execute(f"INSERT INTO users (USERNAME, PASSWORD) VALUES ('{username}', '{password}')")

        conn.commit()

        return redirect("page")
        
    username = ""
    password = ""
    passwordConfirm = ""
    
    return render_template("/pages/register.html")


if __name__ == '__main__':
    app.run()
