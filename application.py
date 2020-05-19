from flask import Flask, render_template

app = Flask(__name__, static_folder='D:\intro to CS\project0\static')

@app.route("/", methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/4year")
def four_year():
    return render_template("4year.html")