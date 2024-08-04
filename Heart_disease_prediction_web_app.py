# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 02:48:08 2024

@author: SHRIYANS
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('heart_prediction.sav', 'rb'))

def main():
    
   
    st.title('Heart Disease Predictor') 
    
    st.caption("The predictor aims to predict any future Heart Disease by analyzing the data of the patient. Kindly refer to the Attribute Information section to know about the required biological parameters.")
    
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain Type')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholesterol') 
    fbs = st.text_input('Fasting Blood Sugar')
    restecg = st.text_input('Resting Electrocardiographic Result')
    thalach = st.text_input('Maximum Heart Rate Achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('Oldpeak')
    slope = st.text_input('Slope of the peak exercise of ST Segment')
    ca = st.text_input('Number of major vessels  colored by fluoroscopy')
    thal = st.text_input('Thalassemia')
    
   
    heart_diagnosis = ''
   
    user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
    
    if st.button('Predict'):
        
        if (age =='' or sex=='' or cp=='' or trestbps=='' or chol=='' or fbs=='' or restecg =='' or thalach=='' or exang=='' or oldpeak=='' or slope=='' or ca=='' or thal==''):
            st.error('Kindly fill all the parameters.')
            
        if (float(age) < 1):
            st.error('Age cannot be negative or zero')
            
        elif(float(sex) < 0 or float(sex) > 1 ):
            st.error('Please enter 0 for female &  1 for male')
            
        elif(float(cp)<0 or float(cp)>3):
            st.error('Chest pain can have only 4 values')
            
        elif(float(chol)<0):
            st.error('Serum cholesterol cannot be negative')
            
        elif(float(fbs)<0 or float(fbs)>1):
            st.error('Please enter 0 for (< 120 mg/dl), otherwise enter 1 ')
            
        elif(float(restecg)<0 or float(restecg)>2):
            st.error('Please enter values from 0-2 for RestECG')
            
        elif(float(thalach)<0):
            st.error('Maximum heart rate achieved cannot be negative')
            
        elif(float(exang)<0):
            st.error('Exercise induced angina cannot be negative')
            
        elif(float(oldpeak)<0):
            st.error('ST depression cannot be negative')
            
        elif(float(slope)<0):
            st.error('Slope cannot be negative')
            
        elif(float(ca)<0 or float(ca)>3):
            st.error('Please enter values from 0-3 for Number of major vessels')
            
        elif(float(thal)<0 or float(thal)>3):
            st.error('Please enter values from 0-3 for Thalassemia')
            
        else:
            user_input = [ float (x) for x in user_input]
            
            heart_prediction = loaded_model.predict([user_input])
        
            if (heart_prediction[0] == 1):
                heart_diagnosis = 'The Person may have a Heart Disease'
                
            else:
                heart_diagnosis = 'The Person does not have a Heart Disease'
                
    st.success(heart_diagnosis)
    
    st.info("Attribute Information:")
    st.caption("1. Age: The person's age in years")
    st.caption("2. Sex: The person's sex (1 = male, 0 = female)")
    st.caption("3. Chest Pain Type: Value 0: asymptomatic, Value 1: atypical angina, Value 2: non-anginal pain, Value 3: typical angina")
    st.caption("4. Resting Blood Pressure: The person's blood pressure in mm Hg")
    st.caption("5. Serum Cholesterol: The person's cholesterol measurement in mg/dl")
    st.caption("6. Fasting Blood Sugar: The person's fasting blood sugar ( > 120 mg/dl, 1 = true; 0 = false)")
    st.caption("7. Resting Electrocardiographic Result: Value 0: showing probable or definite left ventricular hypertrophy by Estes' criteria, Value 1: normal, Value 2: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV")
    st.caption("8. Maximum Heart Rate Achieved: The person's maximum heart rate achieved")
    st.caption("9. Exercise Induced Angina: 1 = yes; 0 = no")
    st.caption("10. Oldpeak: ST Depression induced by exercise relative to rest")
    st.caption('11. Slope: The slope of the peak exercise ST segment - 0: downsloping; 1: flat; 2: upsloping')
    st.caption('12. Number of major vessels (1-4)')
    st.caption("13. Thalassemia: A blood disorder called thalassemia, Value 0: NULL, Value 1: fixed defect, Value 2: normal blood flow, Value 3: reversible defect")

    st.markdown("<p style = 'text-align: center; black: red;'>Created by Shriyans Rout</p>", unsafe_allow_html=True)
    st.markdown("<p style = 'text-align: center; black: grey;'>@ Heartlife-2024</p>", unsafe_allow_html=True)
    
if __name__ == '__main__':
    main()