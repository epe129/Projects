from flask import Flask, render_template, request
from flask_bcrypt import Bcrypt
import json

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/page')
def page(Username2, UserID2):
    return render_template("page.html", Username=Username2, UserID2=UserID2)

@app.route('/', methods =["GET", "POST"])
def home():
    Username = ""
    Password = ""
    hashed_password = ""
    
    if request.method == "POST":
        Username = request.form.get("Username").capitalize()
        Password = request.form.get("Password")
        id = request.form.get("id")

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
                for nimi in value:
                    if Username == nimi["Username"]:
                        tunnus.clear()
                        Username = ""
                        Password = ""
                        hashed_password = ""
            if Username == "" and Password == "":
                pass
            else:
                file_data["tiedot"].append(tunnus)
                    
                f.seek(0)
                    
                json.dump(file_data, f, indent=4)
       

    return render_template("create.html")

@app.route('/Signin', methods =["GET", "POST"])
def Signin():
    
    if request.method == "POST":
        Username2 = request.form.get("Username").capitalize()
        Password2 = request.form.get("Password")
        UserID2 = request.form.get("UserID")

        with open("json.json", "r") as tiedosto:
            data = tiedosto.read()
            tiedot = json.loads(data)
            for key, value in tiedot.items():
                for d in value:
                    getid = d["id"]
                    getusername = d["Username"]
                    getpassword = d["Password"]

                    oikeia = bcrypt.check_password_hash(getpassword, Password2)
                   
                    if UserID2 == getid and Username2 == getusername and oikeia == True:
                        return page(Username2, UserID2)
                    else:
                        print("väärin")
                    Username2 = ""
                    Password2 = ""
                    UserID2 = ""
    return render_template("Signin.html")

@app.route('/admin', methods =["GET", "POST"])
def admin():
    return render_template("admin.html")

if __name__ == '__main__':
     app.run()