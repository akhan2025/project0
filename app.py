from flask import Flask, render_template, request

app = Flask(__name__, static_folder='D:\intro to CS\project0\static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/4year")
def four_year():
    return render_template("4year.html")

@app.route("/professional")
def professional():
    return render_template("professional.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/thankyou", methods=['GET', 'POST'])
def thank_you():
    name = request.form.get("name")
    return render_template("thankyou.html", name=name)