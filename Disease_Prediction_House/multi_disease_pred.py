# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 19:10:57 2025

@author: ADMIN
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the model

obesity_model=pickle.load(open("C:/Users/ADMIN/OneDrive/Desktop/Disease_Prediction_House/saved_model/obesity_prediction.sav",'rb'))

stroke_model=pickle.load(open("C:/Users/ADMIN/OneDrive/Desktop/Disease_Prediction_House/saved_model/StrokePrediction.sav",'rb'))

#sidebar for navigate

with st.sidebar:
    selected = option_menu("Prediction House System",
                           ['Obesity Prediction System',
                               'Stroke Prediction System'],
                              
                              icons=['activity','heart'],
                              default_index=0)
# Diabetes Prediction Page

if(selected=='Obesity Prediction System'):
    st.title('Obesity Prediction')
    Age = st.text_input("Age")
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Height = st.text_input("Height")
    Weight = st.text_input("Weight")
    BMI = st.text_input('BMI')
    PhysicalLevel = st.text_input('Physical Activity Level')
    
    Gender = 0 if Gender == "Male" else 1
        
    
        
    obe_diagnosis = ''
    
    if st.button('Test Result'):
        obe_prediction = obesity_model.predict([[Age,Gender,Height,Weight,BMI,PhysicalLevel]])
        if(obe_prediction[0]==0):
            obe_diagnosis = "Normal Weight"
        elif(obe_prediction[0]==1):
            obe_diagnosis = "Obese"
        elif(obe_prediction[0]==2):
            obe_diagnosis = "Over Weight"
        else:
            obe_diagnosis = "Under Weight"
    st.success(obe_diagnosis)
    
if(selected=='Stroke Prediction System'):
    st.title('Stroke Prediction')
    
    c1,c2,c3 = st.columns(3)
    
    with c1:
        Gender = st.selectbox("Gender", ["Male", "Female"])
    with c2:
        Age = st.text_input("Age")
    with c3:
        tension = st.selectbox("Hypertension", ["No", "Yes"])
        
    with c1:
        Hdisease = st.selectbox("Heart Disease", ["No", "Yes"])
    with c2:
        ever_married = st.selectbox("Married", ["No", "Yes"])
    with c3:
        work_type = st.selectbox(
            "Work Type", 
            ["Govt Job", "Never Worked", "Private", "Self Employ", "Under18"]
        )
        
    with c1:
        Residence = st.selectbox("Residence Type", ["Urban", "Rural"])
    with c2:
        glu_level = st.text_input("Average Glucose level")
    with c3:
        bmi = st.text_input("BMI")
    with c1:
        smoke = st.selectbox("Smoking Habit", ["Nil", "Formally", "Never", "Smokes"])
        
    Gender = 1 if Gender == "Male" else 0
    ever_married = 1 if ever_married == "Yes" else 0
    tension = 1 if tension == "Yes" else 0
    Hdisease = 1 if Hdisease == "Yes" else 0
    Residence = 1 if Residence == "Urban" else 0
    work_map = {
        "Govt Job": 0,
        "Never Worked": 1,
        "Private": 2,
        "Self Employ": 3,
        "Under18": 4
    }
    work_type = work_map[work_type]
    
    smoke_map = {
        "Nil": 0,
        "Formally": 1,
        "Never": 2,
        "Smokes": 3
    }
    smoke = smoke_map[smoke]
        
    

    sto_diagnosis=''
    
    if st.button('Result'):
        sto_prediction= stroke_model.predict([[Gender,Age,tension,Hdisease,ever_married,work_type,Residence,glu_level,bmi,smoke]])
        
        if(sto_prediction[0]==1):
            sto_diagnosis = "Stroke Confirmation"
        else:
            sto_diagnosis="Stroke Discocnfirmation"
            
    st.success(sto_diagnosis)
    
    
        
    



