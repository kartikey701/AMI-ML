from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model (make sure the path is correct)
model = pickle.load(open('randomforest_acute_myocardial_infarction.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collecting input values from the form
        float_features = [float(x) for x in request.form.values()]
        final_features = np.array([float_features])

        # Make prediction using the loaded model
        prediction = model.predict(final_features)

        # Check the prediction result (1 or 0)
        result = prediction[0]

        # Prepare the result and advice based on prediction
        if result == 1:
            advice = "Need to visit dr."
        else:
            advice = "All fine."

        # Redirect to a new page with the result and advice
        return render_template('result.html', result=result, advice=advice)

    except Exception as e:
        # If something goes wrong, print the error and return an error page or message
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
