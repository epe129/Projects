from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/peruslaskuja')
def peruslaskuja():
    return render_template("/pelit/peruslaskut.html")

if __name__ == '__main__':
    app.run(debug=True)