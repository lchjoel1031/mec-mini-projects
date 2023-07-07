# Serve model as a flask application

import pickle
import numpy as np
import pandas as pd
from flask import Flask, request

model = None
app = Flask(__name__)


def load_model():
    global model_hier
    # model variable refers to the global variable
    #with open('iris_trained_model.pkl', 'rb') as f:
    with open('./hierarchical_level_lgbm_model.pkl', 'rb') as f:
        model_hier = pickle.load(f)

    global model_periodic
    # model variable refers to the global variable                                                                                                                               
    #with open('iris_trained_model.pkl', 'rb') as f:                                                                                                                             
    with open('./periodic_level_lgbm_model.pkl', 'rb') as f:
        model_periodic = pickle.load(f)

    global model_stochastic
    # model variable refers to the global variable                                                                                                                               
    #with open('iris_trained_model.pkl', 'rb') as f:                                                                                                                             
    with open('./stochastic_level_lgbm_model.pkl', 'rb') as f:
        model_stochastic = pickle.load(f)

    global model_transient
    # model variable refers to the global variable                                                                                                                               
    #with open('iris_trained_model.pkl', 'rb') as f:                                                                                                                             
    with open('./transient_level_lgbm_model.pkl', 'rb') as f:
        model_transient = pickle.load(f)

        

@app.route('/')
def home_endpoint():
    return 'Welcome to LC classifier!'


@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        print('datain: ')
        datain = request.get_data(as_text=True)  # Get data posted as a json
        print(datain)
        print('data: ')
        data = pd.read_json(datain)  # converts json to pandas
        print(data)
        hier = model_hier.predict(data)  # runs globally loaded model on the data
        print('hierarchical: ')
        print(hier)
        if hier[0] == 'Periodic':
            prediction = model_periodic.predict(data)
        if hier[0] == 'Stochastic':
            prediction = model_stochastic.predict(data)
        if hier[0] == 'Transient':
            prediction = model_transient.predict(data)
        return (hier[0]+': '+prediction[0])


if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)
