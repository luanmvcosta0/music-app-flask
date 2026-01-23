from flask import Flask, render_template, request, redirect, session


class Musica:
    def __init__(self, nome, cantorBanda, genero):
        self.nome = nome
        self.cantorBanda = cantorBanda
        self.genero = genero


musica01 = Musica("Loira de Medicina", "G.A", "Trap")
musica02 = Musica("Papai Banca", "MC Ryan SP", "Funk")
musica03 = Musica("Camisa 10", "Turma do Pagode", "Pagode")

lista = [musica01, musica02, musica03]


app = Flask(__name__)

app.secret_key = "minhachavesecreta"


@app.route("/")
def listar_musicas():
    return render_template("lista_musicas.html", musicas=lista)


@app.route(
    "/adicionar",
    methods=[
        "POST",
    ],
)
def adicionar_musica():
    nome = request.form["txtNome"]
    cantorBanda = request.form["txtCantor"]
    genero = request.form["txtGenero"]

    novaMusica = Musica(nome, cantorBanda, genero)

    lista.append(novaMusica)

    return redirect("/")


@app.route("/cadastrar")
def cadastrar_musica():
    return render_template(
        "cadastra_musica.html",
    )


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/autenticar", methods=["POST"])
def autenticar():
    if request.form["txtSenha"] == "admin":
        session["usuario_logar"] = request.form["txtLogin"]

        return redirect("/")
    else:
        return redirect("login")


app.run(debug=True)
