from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot_py import chatbot_response  # import our new function

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")  # make sure templates/index.html exists

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_msg = data.get("message", "")
    reply = chatbot_response(user_msg)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
