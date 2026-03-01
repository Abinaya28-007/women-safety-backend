from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # IMPORTANT for Netlify frontend

@app.route("/")
def home():
    return "Backend is running successfully!"

@app.route("/sos", methods=["POST"])
def sos():
    try:
        data = request.json
        location = data.get("location", "Unknown location")

        print("🚨 SOS Triggered from:", location)

        return jsonify({
            "status": "success",
            "message": "SOS Triggered Successfully",
            "location": location
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)