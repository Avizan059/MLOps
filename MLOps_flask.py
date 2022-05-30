# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request, render_template 
import numpy as np
import pandas as pd
import flasgger
from flasgger import Swagger
import pickle
import cloudpickle

app = Flask(__name__)
Swagger(app)


pickle_in = open('outcome_2.pkl','rb')
classifier = pickle.load(pickle_in)

drift_fn = cloudpickle.load(open('drift_new.pkl', 'rb'))
@app.route('/')
def welcome():
    return "Welcome you"

@app.route('/predict_file',methods=['POST'])
def predict_value():
    """ Upload the testing File.
    ---  
    parameters:
        - name: file
          in :  formData
          type: file
          required: true
        
    responses:
        200:
            description:    The output value 
            
  
    """
    
    df_test= pd.read_csv(request.files.get('file'))
    prediction=classifier.predict(df_test)
    return str(list(prediction))

@app.route('/Drift',methods=['POST'])
def draft_value():
    """ Upload the testing File.
    ---  
    parameters:
        - name: file
          in :  formData
          type: file
          required: true
          
        - name: file
          in :  formData
          type: file
          required: true
        
    responses:
        200:
            description:    The output value 
            
  
    """
    
    df_test= pd.read_csv(request.files.get('file'))
    df_train = pd.read_csv(request.files.get('file'))
    
    
   
    draft=drift_fn(df_train,df_test)
    
    return render_template('table.html', tables=[draft.to_html()], titles=['']) 
    

if __name__=='__main__':
    app.run()
    














if __name__=='__main__':
    app.run()