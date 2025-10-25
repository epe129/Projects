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
        title = request.form.get("title")
        description = request.form.get("description")
        cooking_time = request.form.get("cooking_time")
        servings = request.form.get("servings")
        category = request.form.get("category")
 
        ingredient_name_1 = request.form.get("ingredient_name_1")
        ingredient_amount_1 = request.form.get("ingredient_amount_1")
 
        ingredient_name_2 = request.form.get("ingredient_name_2")
        ingredient_amount_2 = request.form.get("ingredient_amount_2")
 
        ingredient_name_3 = request.form.get("ingredient_name_3")
        ingredient_amount_3 = request.form.get("ingredient_amount_3")
 
        ingredient_name_4 = request.form.get("ingredient_name_4")
        ingredient_amount_4 = request.form.get("ingredient_amount_4")
 
        ingredient_name_5 = request.form.get("ingredient_name_5")
        ingredient_amount_5 = request.form.get("ingredient_amount_5")
 
        ingredient_name_6 = request.form.get("ingredient_name_6")
        ingredient_amount_6 = request.form.get("ingredient_amount_6")
 
        ingredient_name_7 = request.form.get("ingredient_name_7")
        ingredient_amount_7 = request.form.get("ingredient_amount_7")
 
        ingredient_name_8 = request.form.get("ingredient_name_8")
        ingredient_amount_8 = request.form.get("ingredient_amount_8")
 
        ingredient_name_9 = request.form.get("ingredient_name_9")
        ingredient_amount_9 = request.form.get("ingredient_amount_9")
 
        ingredient_name_10 = request.form.get("ingredient_name_10")
        ingredient_amount_10 = request.form.get("ingredient_amount_10")
 
        
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