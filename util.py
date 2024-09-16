import json
import pickle
import sklearn
import numpy as np
import warnings
import flask
from flask import flask
import streamlit as st
warnings.filterwarnings('ignore')
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bath,bhk):

    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x1 = np.zeros(len(__data_columns))
    x1[0] = sqft
    x1[1] = bath
    x1[2] = bhk
    if loc_index >= 0:
        x1[loc_index] = 1

    return round(__model.predict([x1])[0],2)



def get_location_names ():
    return __locations

def load_saved_artifets():
    print("Server/artifacts/columns.json")
    global __locations
    global __data_columns

    with open("Server/artifects/columns.json", 'r') as f:
       __data_columns = json.load(f)['data_columns']
       __locations = __data_columns[3:]
    global __model
    with open("Server/artifets/banglore_home_prices_model.pickle", 'rb') as f :
        __model = pickle.load(f)
    print("loading artifacts ... done")




if __name__ == '__main__':
    load_saved_artifets()
    print(get_location_names())


if __name__ == '__main__' :
    load_saved_artifets()
    print(get_estimated_price("1st Phase JP Nagar",1000,3,3))
    print(get_estimated_price("1st Phase JP Nagar", 1000, 2, 2))
    print(get_estimated_price("kalhalli", 1000, 3, 3)) # other location
    print(get_estimated_price("Ejipura", 1000, 2, 2)) # other location







