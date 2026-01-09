from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired
from flask_session import Session
import json
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False  
app.config["SESSION_TYPE"] = "filesystem" 
bcrypt = Bcrypt(app)
SECRET_KEY = os.urandom(32)
app.secret_key = SECRET_KEY  
csrf = CSRFProtect(app)  
Session(app)

# Create account
class Register(FlaskForm):
    Username  = StringField('Username', validators=[DataRequired()])
    Password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods =["GET", "POST"])
def home():
    form = Register()

    Username = ""
    Password = ""
    hashed_password = ""
    taken = ""
    
    if request.method == "POST":
        if form.validate_on_submit():
            Username = form.Username.data.lower()
            Password = form.Password.data
            session["Username"] = Username
        else:
            return "Error!"

        if Password != "" and Password is not None:
            hashed_password = bcrypt.generate_password_hash(Password).decode('utf-8')

    if Username == "" or Password == "":
        pass
    else:
        tunnus = {
            "Username": f"{Username}",
            "Password": f"{hashed_password}",
        }
        # fill json with user data
        with open("json.json", "r+") as f:
            file_data = json.load(f)
            for key, value in file_data.items():
                for arvo in value:
                    # if username is taken fails
                    if Username == arvo["Username"]:
                        tunnus.clear()
                        Username = ""
                        Password = ""
                        hashed_password = ""
                        taken = "Username or id is taken"               
            if Username == "" and Password == "":
                pass
            else:
                file_data["tiedot"].append(tunnus)
                    
                f.seek(0)
                    
                json.dump(file_data, f, indent=4)
                
                return redirect(url_for('page', Username=Username))

    return render_template("create.html", taken=taken, form=form)

# Signin
class SigninClass(FlaskForm):
    Username  = StringField('Username', validators=[DataRequired()])
    Password2 = PasswordField('Password', validators=[DataRequired()])
    submit2 = SubmitField('Submit')

@app.route('/Signin', methods =["GET", "POST"])
def Signin():
    form2 = SigninClass()

    wrong = ""
    Username = ""
    Password2 = ""

    if request.method == "POST":
        if form2.validate_on_submit():
            Username = form2.Username.data.lower()
            Password2 = form2.Password2.data

            session["Username"] = Username
            # retrieves user data from json
            with open("json.json", "r") as tiedosto:
                data = tiedosto.read()
                tiedot = json.loads(data)
                for key, value in tiedot.items():
                    for d in value:
                        if d["Username"] == Username:
                            getusername = d["Username"]
                            getpassword = d["Password"]
                            
                            is_valid = bcrypt.check_password_hash(getpassword, Password2)
                            #  check that password, id and username is right
                            if Username in getusername and is_valid == True:                
                                return redirect(url_for('page', Username=Username))
                            else:
                                wrong = "Username, Password or id is wrong!"

                            Username = ""
                            Password2 = ""
                            id = ""
        else:
            return "Error!"

    return render_template("Signin.html", wrong=wrong, form2=form2)

# admin
class adminlogin(FlaskForm):
    name  = StringField('name', validators=[DataRequired()])
    password  = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/adminLogin', methods =["GET", "POST"])
def adminLogin():
    form = adminlogin()
    username = ""
    password = ""

    if request.method == "POST":
        if form.validate_on_submit():
            username = form.name.data
            password = form.password.data
            session["Username"] = username
            with open("admin.json", "r") as tiedosto:
                data = tiedosto.read()
                tiedot = json.loads(data)
                for key, value in tiedot.items():
                    for d in value:
                        if d["Username"] == username:
                            getusername = d["Username"]
                            getpassword = d["Password"]
                            
                            if getusername == username and getpassword == password:                 
                                return redirect(url_for('adminPage', username=username))
                            else:
                                pass
                            username = ""
                            password = ""
        else:
            return "Error!"

    return render_template("adminLogin.html", form=form)

class adiminP(FlaskForm):
    poista  = StringField('poista', validators=[DataRequired()])
    submit3 = SubmitField('Submit')

# admin can delete user and see all users
@app.route('/adminPage/<username>', methods =["GET", "POST"])
def adminPage(username):
    form = adiminP()

    kayttajat = []
    print(username)
    if not session.get("Username"):
        return redirect("/adminLogin")
    
    with open("json.json", "r") as tiedosto:
        data = tiedosto.read()
        tiedot = json.loads(data)
        for key, value in tiedot.items():
            for d in value:
                kayttajat.append(d)

    return render_template("admin.html", kayttajat=kayttajat, form=form, username=username)


# page
class blog(FlaskForm):
    title  = StringField('title', validators=[DataRequired()])
    text  = TextAreaField('text', render_kw={'rows': 10, 'cols': 50}, validators=[DataRequired()])
    submit3 = SubmitField('Submit')

@app.route('/page/<Username>', methods =["GET", "POST"])
def page(Username):
    blogs(Username)
    if not session.get("Username"):
        return redirect("/Signin")

    form = blog()
    title = ""
    text = ""

    if request.method == "POST":
        if form.validate_on_submit():
            title = form.title.data
            text = form.text.data
        else:
            return "Error!"

    if title == "" or text == "":
        pass
    else:        
        Write_blog = {
            "username": f"{Username}",
            "title": f"{title}",
            "text": f"{text}"
        }
        # appends blog in json file
        with open("blog.json", "r+") as f:
            file_data = json.load(f)
            for key, value in file_data.items():
                for a in value:
                    if a["Username"] == Username and a["title"] == title:
                        title = ""
                        text = ""
            
            if title == "" or text == "":
                pass
            else:
                file_data["blogit"].append(Write_blog)
                            
                f.seek(0)
                            
                json.dump(file_data, f, indent=4)              

    return render_template('page.html', Username=Username, form=form)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# blogs

class poistablog(FlaskForm):
    blogin_title  = StringField('blogin_title', validators=[DataRequired()])
    submit = SubmitField('submit')

@app.route("/blogs/<Username>", methods =["GET", "POST"])
def blogs(Username):
    HerBlogs = []
    poista = ""
    form = poistablog()

    # can delete blog
    if request.method == "POST":
        if form.validate_on_submit():
            poista = form.blogin_title.data
            updated_data = {}
            updated_data2 = {
                "blogit": [
                ]
            }
            if poista == "":
                pass
            else:
                with open("blog.json", "r+") as tiedosto:
                    data = tiedosto.read()
                    tiedot = json.loads(data)
                    for key, value in tiedot.items():
                        for d in value:
                            if d["title"] == poista:
                                d.pop("title")
                                d.pop("text")
                            else:                  
                                updated_data.update({key : value})
                
                for c , s in updated_data.items():
                    for w in s:
                        if bool(w) == False:
                            continue
                        else:
                            updated_data2["blogit"].append(w)

                with open('blog.json', 'w') as file:
                    json.dump(updated_data2,file,indent=2)
        else:
            return "Error!"

    # retrieves blogs from a json file
    with open("blog.json", "r+") as f:
        file_data = json.load(f)
        for key, value in file_data.items():
            for result in value:
                if result["username"] == str(Username):
                    HerBlogs.append(result)
                else:
                    continue

    return render_template("blogs.html", Username=Username, result=HerBlogs, p=len(HerBlogs), form=form)

if __name__ == '__main__':
    app.run(debug=True)
