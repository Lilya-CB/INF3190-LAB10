from flask import Flask
from flask import render_template
from flask import request
from flask import redirect,url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("labFlask2.html")





















@app.route("/validate", methods=["POST"])
def validate():
    error = ""
    nom = request.form["nom"];
    prenom = request.form["prenom"];
    age = request.form["age"];

    # return f"{nom} {prenom} {age}"

    if not nom or not nom.strip():
        error += "Vous devez entrer un nom \n" 

    if not prenom or not prenom.strip():
        error += "Vous devez entrer un prenom \n"

    if not age or not age.strip():
        error += "Vous devez entrer l'âge \n"

    if error:
        return render_template("labFlask2.html", error=error, nom=nom, prenom=prenom, age=age)

    with open("db.txt", 'a') as file:
        file.write(f"{nom}, {prenom}, {age}\n")

    return redirect(url_for("result"))





@app.route("/result")
def result():
    records = []
    with open("db.txt", 'r') as file:
        lines = file.readlines()

        for line in lines:
            record = line.split(",")
            records.append(record)

    return render_template("results.html", records=records, len=len(records))


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404