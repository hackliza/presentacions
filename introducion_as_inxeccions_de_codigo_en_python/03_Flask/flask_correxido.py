from flask import render_template, Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    nome = request.args.get('nome')
    return render_template('template.html', nome=nome)


if __name__ == "__main__":
    app.run()
