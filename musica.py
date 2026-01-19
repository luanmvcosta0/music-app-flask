from flask import Flask, render_template

app = Flask(__name__)


@app.route("/musicas")
def listar_musicas():

    lista = ["KGL", "Loira de medicina", "Havaiana Branca", "Ousadia e Alegria"]

    return render_template("lista_musicas.html", musicas=lista)


app.run(debug=True)
