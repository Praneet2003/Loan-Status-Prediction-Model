from flask import Flask, request, jsonify
import pickle
import numpy as np

with open('random_forest.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    features = [float(x) for x in data.values()]
    final_features = [np.array(features)]

    prediction = model.predict(final_features)

    output = (
        "🎉 Congratulations! Your loan can be sanctioned"
        if prediction[0] == 1
        else "❌ Sorry! Your loan cannot be sanctioned"
    )

    return jsonify({
        "prediction": output
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)