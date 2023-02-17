from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template("index.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    data = dict()
    print(prof)
    if "инженер" in prof.lower():
        data["work"] = "Инженерные тренажеры"
        data["src"] = url_for('static', filename="img/ingener.jpg")
        data["alt"] = "тут инженерная картинка"

    elif "строитель" in prof.lower():
        data["work"] = "Строительные тренажеры"
        data["src"] = url_for('static', filename="img/builder.jpg")
        data["alt"] = "тут строительная картинка"

    else:
        data["work"] = "Научные симуляторы"
        data["src"] = url_for('static', filename="img/sciene.jpg")
        data["alt"] = "тут научная картинка"
    print(data["src"])
    return render_template("index.html", **data)


if __name__ == "__main__":
    app.run()
