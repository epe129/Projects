from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def index():
    r = []

    with open("recepies.json", "r+") as f:
        file_data = json.load(f)
        for key, value in file_data.items():
            for result in value:
                r.append(result)

    if request.method == "POST":
        print("moi") 
    
    return render_template("index.html", r=r)

@app.route('/recepies/<id>', methods=['GET', "POST"])
def recepies_page(id):
    resepti = []

    with open("recepies.json", "r+") as f:
        file_data = json.load(f)
        for key, value in file_data.items():
            for result in value:
                if str(id) in str(result["id"]):
                    resepti.append(result)

    return render_template("recepies.html", r=resepti)


if __name__ == '__main__':
    app.run()