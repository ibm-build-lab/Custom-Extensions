from flask import Flask, jsonify

PORT = 5000

app = Flask(__name__)

languages = [
    "English", "Spanish", "French", "German", "Italian", "Portuguese", "Swedish"
]

@app.route("/")
def home():
    return jsonify({
        "status": "online"
    })

@app.route("/languages")
def get_languages():
    return jsonify({
        "languages": languages
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
