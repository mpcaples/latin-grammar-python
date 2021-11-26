from flask import Flask, render_template
from grammar import generate_sentence

app = Flask(__name__)

@app.route("/")
def sentence():
    sentence = generate_sentence()
    return render_template("home.html", sentence=sentence)
    
if __name__ == "__main__":
    app.run(debug=True)