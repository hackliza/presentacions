from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    nome = request.args.get('nome')
    template = f"""
<!doctype html>
<title>Saudos</title>
<section class="content">
    <b>Escribe o teu nome:</b>
    <form method="get">
        <input name="nome" id="nome" required>
        <input type="submit" value="Enviar">
    </form>
    {"Bos días " + nome + "!" if nome else ""}
</section>
    """
    return render_template_string(template)


if __name__ == "__main__":
    app.run()
