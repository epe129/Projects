# this is test project i don't care if you see the data 

from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

@app.route('/page')
def page(Username2):
    return render_template("page.html", Username=Username2)

@app.route('/', methods =["GET", "POST"])
def home():
    id = random.randint(1, 100)
    Username = ""
    Password = ""

    if request.method == "POST":
        Username = request.form.get("Username")
        Password = request.form.get("Password")
    
    if Username == "" or Password == "":
        pass
    else:
        tunnus = {
            "id": f"{id}",
            "Username": f"{Username}",
            "Password": f"{Password}",
        }

        with open("json.json", "r+") as f:
            file_data = json.load(f)
                
            file_data["tiedot"].append(tunnus)
                
            f.seek(0)
                
            json.dump(file_data, f, indent=4)
        tunnus.clear()
        Username = ""
        Password = ""
    return render_template("index.html", id=id)

@app.route('/Singin', methods =["GET", "POST"])
def Singin():
    
    if request.method == "POST":
        Username2 = request.form.get("Username")
        Password2 = request.form.get("Password")
        UserID2 = request.form.get("UserID")
        # print(Username, Password, UserID)
        with open("json.json", "r") as tiedosto:
            data = tiedosto.read()
            tiedot = json.loads(data)
            for key, value in tiedot.items():
                for d in value:
                    getid = d["id"]
                    getusername = d["Username"]
                    getpassword = d["Password"]
                   
                    if UserID2 == getid and Username2 == getusername and Password2 == getpassword:
                        print("True")
                        return page(Username2)
                    else:
                        print("väärin")
                    Username2 = ""
                    Password2 = ""
                    UserID2 = ""
    return render_template("Singin.html")


if __name__ == '__main__':
     app.run()