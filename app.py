from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

data_dict = {"base-servo": 0}

@app.route("/")
def hello():
    return render_template("form.html")

@app.route("/submit", methods=["POST", "GET"])
def submit():
    data_dict["base-servo"] = request.form["user"]
    return redirect(url_for("hello"))

@app.route("/<key>")
def get_data_by_key(key):
    return str(data_dict[key])

@app.route("/data")
def data():
    return data_dict
