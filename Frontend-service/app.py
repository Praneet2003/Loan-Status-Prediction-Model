from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    data = request.form.to_dict()

    response = requests.post(
        'http://predictor:5001/predict',
        json=data
    )

    prediction = response.json()['prediction']

    requests.post(
        'http://logger:5002/log',
        json={
            "input": data,
            "result": prediction
        }
    )

    return render_template(
        'index.html',
        prediction_text=prediction,
        form_values=request.form
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)