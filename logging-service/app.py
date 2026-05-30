from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():

    with open("logs.txt", "a") as f:
        f.write(
            f"{datetime.now()} : {request.json}\n"
        )

    return jsonify({
        "status": "logged"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)