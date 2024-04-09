'''from flask import Flask,redirect,url_for,jsonify,render_template,request
import pickle
import numpy as np

app=Flask(__name__)
model = pickle.load(open('randomforest_acute_myocardial_infarction.pkl','rb'))

@app.route('/')  #iss page rr jaunga toh ye def wel wala function trigger ho jayega
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    float_features  = [int(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
 
    return render_template('index.html',prediction_text = 'it is  {}'.format(prediction))


@app.route('/predict_api',methods = ['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug = True)'''

from flask import Flask, redirect, url_for, jsonify, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('randomforest_acute_myocardial_infarction.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Convert form values to integers
    float_features = [int(x) for x in request.form.values()]
    
    # Log the int_features variable
    print("int_features:", float_features)

    # Convert to numpy array
    final_features = [np.array(float_features)]
    
    # Make prediction
    prediction = model.predict(final_features)
 
    return render_template('index.html', prediction_text='The prediction is {}'.format(prediction))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    # Get JSON data from request
    data = request.get_json(force=True)
    
    # Make prediction
    prediction = model.predict([np.array(list(data.values()))])
    
    # Return prediction as JSON
    return jsonify(prediction[0])

if __name__ == '__main__':
    app.run(debug=True)