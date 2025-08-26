from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
import json

app = Flask(__name__)
bcrypt = Bcrypt(app)

ui = []

@app.route('/page/<Username2>/<UserID2>', methods =["GET", "POST"])
def page(Username2, UserID2):
    ui.append(Username2)
    ui.append(UserID2)

    return render_template("page.html", Username=Username2, UserID2=UserID2)

@app.route('/blogi', methods =["GET", "POST"])
def blogi():
    
    Username2 = ui[0]
    UserID2 = ui[1]

    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")
        print(title)
        print(text)
        print(ui)    
            
    blogi = {
        f"{UserID2}": {"title": f"{title}", "text": f"{text}"}
    }
    
    with open("blog.json", "r+") as f:
        file_data = json.load(f)
    
        file_data["blogit"].append(blogi)
                    
        f.seek(0)
                    
        json.dump(file_data, f, indent=4)                
        
    return redirect(url_for('page', Username2=Username2, UserID2=UserID2)), ui.clear()


@app.route('/', methods =["GET", "POST"])
def home():
    Username = ""
    Password = ""
    hashed_password = ""
    taken = ""
    
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
                
                return redirect(url_for('page', Username2=Username, UserID2=id))

    return render_template("create.html", taken=taken)

@app.route('/Signin', methods =["GET", "POST"])
def Signin():
    wrong = ""
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
                        return redirect(url_for('page', Username2=Username2, UserID2=UserID2))
                    else:
                        wrong = "Username, Password or id is wrong!"
                    Username2 = ""
                    Password2 = ""
                    UserID2 = ""
    return render_template("Signin.html", wrong=wrong)

# I haven't started doing this yet.
@app.route('/admin', methods =["GET", "POST"])
def admin():
    return render_template("admin.html")

if __name__ == '__main__':
     app.run(debug=True)