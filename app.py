# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import flask
import requests
import pickle
from flask import Flask, request, render_template
import numpy as np

app = flask.Flask(__name__)
#Load the trained model. (Pickle file)
model = pickle.load(open('models/model.pkl', 'rb'))

#to display the connection status
@app.route('/', methods=['GET'])
def handle_call():
    return "Successfully Connected"

@app.route('/')
def home():
    return render_template('index.html')

#the get method. when we call this, it just return the text "Hey!! I'm the fact you got!!!"

#the post method. when we call this with a string containing a name, it will return the name with the text "I got your name"


@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()] #Convert string inputs to float.
    features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
    prediction = model.predict(features)  # features Must be in the form [[a, b]]

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Percent with heart disease is {}'.format(output))


#this commands the script to run in the given port
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
