from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
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



class Register(FlaskForm):
    Username  = StringField('Username', validators=[DataRequired()])
    Password = StringField('Password', validators=[DataRequired()])
    id = StringField('id', validators=[DataRequired()])
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
            id = form.id.data
            session["id"] = id

        else:
            return "Error!"

        if Password != "" and Password is not None:
            hashed_password = bcrypt.generate_password_hash(Password).decode('utf-8')

    if Username == "" or Password == "":
        pass
    else:
        tunnus = {
            "id": f"{id}",
            "Username": f"{Username}",
            "Password": f"{hashed_password}",
        }
        with open("json.json", "r+") as f:
            file_data = json.load(f)
            for key, value in file_data.items():
                for arvo in value:
                    if Username == arvo["Username"] or id == arvo["id"]:
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
                
                return redirect(url_for('page', Username=Username, id=id))

    return render_template("create.html", taken=taken, form=form)

class SigninClass(FlaskForm):
    Username  = StringField('Username', validators=[DataRequired()])
    Password2 = StringField('Password', validators=[DataRequired()])
    id2 = StringField('id', validators=[DataRequired()])
    submit2 = SubmitField('Submit')

@app.route('/Signin', methods =["GET", "POST"])
def Signin():
    form2 = SigninClass()

    wrong = ""
    Username = ""
    Password2 = ""
    id = ""

    if request.method == "POST":
        if form2.validate_on_submit():
            Username = form2.Username.data.lower()
            Password2 = form2.Password2.data
            id = form2.id2.data
            session["id"] = id
            
            with open("json.json", "r") as tiedosto:
                data = tiedosto.read()
                tiedot = json.loads(data)
                for key, value in tiedot.items():
                    for d in value:
                        if d["Username"] == Username:
                            getid = d["id"]
                            getusername = d["Username"]
                            getpassword = d["Password"]
                            
                            is_valid = bcrypt.check_password_hash(getpassword, Password2)

                            if str(id) in getid and Username in getusername and is_valid == True:                
                                return redirect(url_for('page', Username=Username, id=id))
                            else:
                                wrong = "Username, Password or id is wrong!"

                            Username = ""
                            Password2 = ""
                            id = ""
        else:
            return "Error!"
    
    return render_template("Signin.html", wrong=wrong, form2=form2)

# I haven't started doing this yet.
@app.route('/admin', methods =["GET", "POST"])
def admin():
    return render_template("admin.html")

class blog(FlaskForm):
    title  = StringField('title', validators=[DataRequired()])
    text  = TextAreaField('text', render_kw={'rows': 10, 'cols': 50}, validators=[DataRequired()])
    submit3 = SubmitField('Submit')

@app.route('/page/<Username>/<id>', methods =["GET", "POST"])
def page(Username, id):
    blogs(Username, id)
    if not session.get("id"):
        return redirect("/Signin")

    form3 = blog()
    title = ""
    text = ""

    if request.method == "POST":
        if form3.validate_on_submit():
            title = form3.title.data
            text = form3.text.data
            print(title)
            print(text)

    if title == "" or text == "":
        pass
    else:        
        Write_blog = {
            "id": f"{id}", 
            "title": f"{title}",
            "text": f"{text}"
        }
        
        with open("blog.json", "r+") as f:
            file_data = json.load(f)
            for key, value in file_data.items():
                for a in value:
                    if a["id"] == id and a["title"] == title and a["text"] == text:
                        title = ""
                        text = ""
            
            if title == "" or text == "":
                pass
            else:
                file_data["blogit"].append(Write_blog)
                            
                f.seek(0)
                            
                json.dump(file_data, f, indent=4)              
                
    return render_template('page.html', Username=Username, id=id, form3=form3)

@app.route("/logout")
def logout():
    session["id"] = None
    return redirect("/")

# make it that can delete blog
@app.route("/blogs/<Username>/<id>")
def blogs(Username, id):
    HerBlogs = []
    
    with open("blog.json", "r+") as f:
        file_data = json.load(f)
        for key, value in file_data.items():
            for result in value:
                if result["id"] == str(id):
                    HerBlogs.append(result)
                else:
                    continue
   
    return render_template("blogs.html", Username=Username, id=id, result=HerBlogs, p=len(HerBlogs))


if __name__ == '__main__':
     app.run(debug=True)