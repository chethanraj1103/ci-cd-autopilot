from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "CI/CD Auto-Pilot Demo API"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json() or {}
    value = data.get("x", 0)
    # trivial "model": multiply by 2
    result = {"y": value * 2}
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
