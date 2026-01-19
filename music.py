from flask import Flask

app = Flask(__name__)


@app.route("/inicio")
def hello():
    return "Ola mundo"


app.run()
