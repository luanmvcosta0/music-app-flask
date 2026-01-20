from flask import Flask, render_template


class Musica:
    def __init__(self, nome, cantorBanda, genero):
        self.nome = nome
        self.cantorBanda = cantorBanda
        self.genero = genero


app = Flask(__name__)


@app.route("/musicas")
def listar_musicas():

    musica01 = Musica("Loira de Medicina", "G.A", "Trap")
    musica02 = Musica("Papai Banca", "MC Ryan SP", "Funk")
    musica03 = Musica("Camisa 10", "Turma do Pagode", "Pagode")

    lista = [musica01, musica02, musica03]

    return render_template("lista_musicas.html", musicas=lista)

@app.route("/cadastrar")


app.run(debug=True)
