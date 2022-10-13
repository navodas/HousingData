#from asyncio.windows_events import NULL
import pathlib
from flask import Flask
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn import preprocessing
import pickle
import json




app = Flask(__name__)

#load model
model = pickle.load(open(pathlib.Path.joinpath(pathlib.Path(__file__).parent,'lr_predictor.pkl'), 'rb'))

#get mean and sd for data preprocessing 
with open(pathlib.Path.joinpath(pathlib.Path(__file__).parent, 'mean_sd.json')) as json_f:
    mean_sd_dict = json.load(json_f)

@app.route("/")
def page_load():
    return(render_template('index.html'))
 
def standadize_data (df, m_df,sd_df):
    return (float(df) - m_df)/sd_df



@app.route('/predict',methods=['POST'])
def predict():

    #load form data    
    feature_dict = request.form.to_dict()

    #data pre-processing
    #Null value handling 
    #median floor
    if feature_dict['floors']=="":
        feature_dict['floors']= "2"
    #median constructed_year
    if feature_dict['constructed_year']=="":
        feature_dict['constructed_year']= "1961"
    #if not specified operational cost is assunmed as 0
    if feature_dict['operating_cost']=="":
        feature_dict['operating_cost']= "0"

    #align attribute names
    new_dict_keys = ['askingprice', 'monthly_fee', 'municipality_tax', 'num_rooms', 'constructed_year', 'operating_cost', 'floors',  'listed_year' ]
    updated_mean_sd_dict = dict(zip(new_dict_keys, list(mean_sd_dict.values())))



    #numerical data standadization
    for key, val in updated_mean_sd_dict.items():
        std_val = standadize_data(feature_dict[key], updated_mean_sd_dict[key][0], updated_mean_sd_dict[key][1])
        feature_dict[key] = std_val

    #data orddering
    feature_list = [feature_dict['askingprice'], feature_dict['monthly_fee'], feature_dict['agent'], feature_dict['municipality'], feature_dict['municipality_tax'], feature_dict['num_rooms'], feature_dict['house_type'], feature_dict['balcony'], feature_dict['constructed_year'], feature_dict['operating_cost'], feature_dict['letting_form'], feature_dict['floors'], feature_dict['lift'], feature_dict['listed_year']]
    feature_list = list(map(float, feature_list))
    final_features = np.array(feature_list).reshape(1,-1)
    print(final_features)
    
    final_features = final_features[0]
    
    #prediction
    prediction = model.predict(final_features.reshape(1,-1))
    result = int(prediction[0])

    return render_template('index.html', predicted_price='Predicted sale price is  SEK {}'.format(result))

if __name__ == "__main__":
    app.run(debug=True)