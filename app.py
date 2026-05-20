# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load trained model
model_path = 'random_forest.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]

        prediction = model.predict(final_features)
        output = '🎉 Congratulations! Your loan can be sanctioned' if prediction[0] == 1 else '❌ Sorry! Your loan cannot be sanctioned'

        return render_template('index.html', prediction_text=output, form_values=request.form)

    except ValueError:
        return render_template('index.html', prediction_text="⚠️ Please enter valid numeric values!", form_values=request.form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
