from flask import Flask, render_template

app = Flask(__name__)


@app.route("/musicas")
def listar_musicas():
    return render_template("lista_musicas.html")


app.run()
