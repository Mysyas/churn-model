#from flask import Flask
import numpy as np
import pickle

#app=Flask(__name__)


def predict(phone,gender,married,satisfaction,internet,download):
    to_predict = np.array([phone,gender,married,satisfaction,download,internet]).reshape(1,6)
    with open('churn_model.pkl','rb') as f:
        model = pickle.load(f)
        y=model.predict(to_predict)
        return "Le client va churner" if y[0]==1 else "Le client ne va pas churner"
    return "erreur"

#if __name__ == '__main__': 
  
#    app.run(debug = True,port=8501) 

