from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow frontend calls from any domain

@app.route("/")
def home():
    return "Backend is running successfully!"

# Dummy AI Risk Predictor
@app.route("/predict-risk", methods=["POST"])
def predict_risk():
    try:
        data = request.get_json()
        lat = float(data.get("latitude", 0))
        lon = float(data.get("longitude", 0))
        hour = int(data.get("hour", 12))
        day = int(data.get("day", 1))

        # Simple logic for demonstration
        if lat > 13.1:
            risk_level = "High"
        elif lon > 80.3:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        return jsonify({"risk_level": risk_level})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# SOS Alert
@app.route("/sos", methods=["POST"])
def sos():
    try:
        data = request.get_json()
        lat = data.get("latitude", "Unknown")
        lon = data.get("longitude", "Unknown")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"🚨 SOS Alert! Location: {lat}, {lon} at {timestamp}")

        return jsonify({
            "status": "success",
            "message": "SOS Triggered Successfully",
            "latitude": lat,
            "longitude": lon,
            "time": timestamp
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)