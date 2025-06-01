from flask import Flask, request, jsonify
import joblib  # or pickle, if you have a model file

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = "mock_prediction"
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)