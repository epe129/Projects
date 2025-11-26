# muuta txt json

from flask import Flask, render_template, redirect, url_for, request
import json

app = Flask(__name__)

te = []

@app.route("/", methods=["GET", "POST"])
def main():
    # GET myös jotta lataa tehtävät heti kun avaa sivun
    if request.method == "POST" or request.method == "GET":
        tehtävä = request.form.get("todoitem")
        
        uusi_tehtava = {
            "tehtava": f"{tehtävä}",
        }

        with open("tekematta.json", "r+") as tiedot:
            file_data = json.load(tiedot)
            
            file_data["tehtavat"].append(uusi_tehtava)
            
            tiedot.seek(0)
            
            json.dump(file_data, tiedot, indent=4)
        
        with open("tekematta.json") as f:
            file_data2 = json.load(f)
            for key, value in file_data2.items():
                for c in value:
                    if c["tehtava"] in te or c["tehtava"] == None or c["tehtava"] == "None":
                        continue
                    else:
                        te.append(c["tehtava"])

    return render_template("main.html",lukee = te, pituus = len(te))
 
@app.route("/poista", methods=["GET", "POST"])
def poista():
    updated_data = {}
    
    updated_data2 = {
        "tehtavat": [

        ]
    }

    if request.method == "POST":

        poista = request.form.get("deleteitem")

        for c in te:
            if poista in c:

                paikka = te.index(c)

                te.pop(paikka)

                with open("tekematta.json") as f:
                    file_data = json.load(f)

                    for key, value in file_data.items():
                        for c in value:
                            if poista == c["tehtava"]:
                                c.pop("tehtava")
                            else:
                                updated_data.update({key : value})
                
                for c , s in updated_data.items():
                    for w in s:
                        if bool(w) == False:
                            continue
                        else:
                            updated_data2["tehtavat"].append(w)
                                
                with open('tekematta.json', 'w') as file:
                    json.dump(updated_data2,file,indent=2)
            
            else:
                pass
    
    return render_template("main.html",lukee = te, pituus = len(te))

if __name__ == '__main__':  
   app.run()  