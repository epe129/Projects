from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/peruslaskuja')
def peruslaskuja():
    return render_template("/pelit/peruslaskut.html")

@app.route('/peruslaskuja/Pluslaskuja')
def Pluslaskuja():
    return render_template("/pelit/Pluslaskuja.html")

@app.route('/peruslaskuja/Miinuslaskuja')
def Miinuslaskuja():
    return render_template("/pelit/Miinuslaskuja.html")

@app.route('/peruslaskuja/Kertolaskuja')
def Kertolaskuja():
    return render_template("/pelit/Kertolaskuja.html")

@app.route('/peruslaskuja/Jakolaskuja')
def Jakolaskuja():
    return render_template("/pelit/Jakolaskuja.html")

if __name__ == '__main__':
    app.run(debug=True)