from flask import Flask, render_template, jsonify 
from flask_cors import CORS 
from grammar import generate_sentence

app = Flask(__name__)
CORS(app) 

@app.route("/")
def sentence():
    sentence = generate_sentence()["sentence"]
    return render_template("home.html", sentence=sentence)

@app.route("/api/sentence", methods=["GET", "POST"])
def api_sentence():
    sentence_dict = generate_sentence()
    sentence = sentence_dict["sentence"]
    sentence_info = sentence_dict["sentence_info_dict"]
    return jsonify(sentence=sentence, sentence_info=sentence_info)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')