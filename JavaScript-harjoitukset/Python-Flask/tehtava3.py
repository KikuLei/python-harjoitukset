from flask import Flask, jsonify, request
from pathlib import Path
import json

app = Flask(__name__)

file = Path(__file__).with_name("dictionary.json")


@app.route("/add")
def add_word():
    english = request.args.get("en", "").strip().lower()
    finnish = request.args.get("fi", "").strip().lower()

    if not english or not finnish:
        return jsonify({
            "error": "Missing word"
        }), 400

    with open(file, encoding="utf-8") as f:
        dictionary = json.load(f)

    dictionary[english] = finnish

    with open(file, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, indent=4,
                  ensure_ascii=False)

    return jsonify({
        "English": english,
        "Finnish": finnish,
        "message": "Word added"
    })


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


if __name__ == "__main__":
    app.run(port=3000)