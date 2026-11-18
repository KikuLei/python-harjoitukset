from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/prime_number/<int:number>")
def prime_number(number):
    is_prime = number > 1

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    return jsonify({
        "Number": number,
        "isPrime": is_prime
    })


if __name__ == "__main__":
    app.run(port=3000)