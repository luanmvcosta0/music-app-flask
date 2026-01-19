from flask import Flask, render_template

app = Flask(__name__)


@app.route("/inicio")
def hello():
    return "Ola mundo"


@app.route("/musicas")
def listar_musicas():
    return render_template("lista_musicas.html")


app.run()
