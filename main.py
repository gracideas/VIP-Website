from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/galeria")
def galeria():
    return render_template("galeria.html", title="Galeria")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html", title="Kontakt")

@app.route("/technologie")
def technologie():
    return render_template("technologie.html", title="Technologie")

@app.route("/blog") # This is just here for testing
def blog():
    return render_template("blog.html", title="Blog")

if __name__ == "__main__":  # Lets you see the changes live 
    app.run(debug=True)