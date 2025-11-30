from flask import Flask, render_template, request
import requests
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['POST', "GET"])
def search():
    vastaus = ""
    if request.method == "POST":
        kysymys = request.form.get("hae")
            
        title = urllib.parse.quote(kysymys)

        url = f"https://fi.wikipedia.org/api/rest_v1/page/summary/{title}"

        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

        if r.status_code != 200:
            return "En löytänyt vastausta."

        data = r.json()

        if "extract" in data and data["extract"]:
            vastaus = data["extract"]


    
    return render_template("index.html", vastaus=vastaus)

if __name__ == '__main__':
    app.run()