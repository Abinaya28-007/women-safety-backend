from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS

# Test route (VERY IMPORTANT)
@app.route('/')
def home():
    return "Backend is running successfully!"

# Risk Prediction API
@app.route('/predict-risk', methods=['POST'])
def predict_risk():
    data = request.get_json()

    lat = float(data.get('latitude'))
    lon = float(data.get('longitude'))
    hour = data.get('hour')
    day = data.get('day')

    # Simple demo logic
    if lat > 13.1:
        risk_level = "High"
    elif lon > 80.3:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return jsonify({"risk_level": risk_level})

# SOS Alert API
@app.route('/send-alert', methods=['POST'])
def send_alert():
    data = request.get_json()

    lat = data.get('latitude')
    lon = data.get('longitude')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"SOS Alert! Location: {lat}, {lon} at {timestamp}")

    return jsonify({
        "status": "success",
        "message": "SOS alert received"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    app.run(debug=True)