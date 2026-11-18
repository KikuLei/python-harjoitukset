from flask import Flask, jsonify
from pathlib import Path
import json

app = Flask(__name__)

file = Path(__file__).with_name("dictionary.json")


@app.route("/translate/<word>")
def translate(word):
    with open(file, encoding="utf-8") as f:
        dictionary = json.load(f)

    word = word.lower()

    if word in dictionary:
        return jsonify({
            "English": word,
            "Finnish": dictionary[word]
        })

    return jsonify({
        "error": "Word not found"
    }), 404


@app.route("/words")
def words():
    with open(file, encoding="utf-8") as f:
        dictionary = json.load(f)

    return jsonify(list(dictionary.keys()))


if __name__ == "__main__":
    app.run(port=3000)