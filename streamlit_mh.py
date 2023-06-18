import streamlit as st
import joblib
import pandas as pd

st.write("# Mental Health Prediction")

col1, col2, col3 ,col4 = st.columns(4)

Age = col2.number_input("Enter your age")
Gender = col1.selectbox("Enter your gender",[ "Female","Male", "Trans"])
family_history = col3.selectbox("Does your family have a history of mental health issues?",["No", "Yes"])
benefits = col4.selectbox("Does your employer provide good amount of benefits?",["Dont know","No", "Yes"])
care_options = col1.selectbox("Do you have access to adequate care options?",["No","Not Sure", "Yes"])
anonymity = col3.selectbox("Do you feel like you need to hide your mental problems?",["Maybe","No", "Yes"])
leave = col2.selectbox("How easy is it to apply for leaves in your company?",["Dont know", 'Somewhat difficult', 'Somewhat easy', 'Very difficult', 'Very easy'])
work_interfere = col4.selectbox("Is your work affecting your personal life?",["Dont know", 'Never', 'Often', 'Rarely', 'Sometimes'])


df_pred = pd.DataFrame([[Age,Gender,family_history,benefits,care_options,anonymity,leave,work_interfere]],

columns= ['Age','Gender','family_history','benefits','care_options','anonymity','leave','work_interfere'])

def transform(gender):
    result = 3
    if(gender=='Female'):
        result = 0
    elif(gender=='Male'):
        result = 1
    elif(gender=='Trans'):
        result = 2
    return(result)
df_pred['Gender'] = df_pred['Gender'].apply(transform)

df_pred['family_history'] = df_pred['family_history'].apply(lambda x: 1 if x == 'Yes' else 0)

def transform(Benefits):
    result = 3
    if(benefits=='Dont know'):
        result = 0
    elif(Benefits=='No'):
        result = 1
    elif(Benefits=='Yes'):
        result = 2
    return(result) 
df_pred['benefits'] = df_pred['benefits'].apply(transform)

def transform(careoptions):
    result = 3
    if(careoptions=='No'):
        result = 0
    elif(careoptions=='Not Sure'):
        result = 1
    elif(careoptions=='Yes'):
        result = 2
    return(result) 
df_pred['care_options'] = df_pred['care_options'].apply(transform)

def transform(anonymity):
    result = 3
    if(anonymity=='No'):
        result = 0
    elif(anonymity=='Maybe'):
        result = 1
    elif(anonymity=='Yes'):
        result = 2
    return(result) 
df_pred['anonymity'] = df_pred['anonymity'].apply(transform)

def transform(leave):
    result = 5
    if(leave=='Dont know'):
        result = 0
    elif(leave=='Very easy'):
        result = 1
    elif(leave=='Somewhat easy'):
        result = 2
    elif(leave=='Somewhat difficult'):
        result = 3
    elif(leave=='Very difficult'):
        result = 4
    return(result)
df_pred['leave'] = df_pred['leave'].apply(transform)

def transform(work_interfere):
    result = 5
    if(work_interfere=='Dont know'):
        result = 0
    elif(work_interfere=='Never'):
        result = 1
    elif(work_interfere=='Rarely'):
        result = 2
    elif(work_interfere=='Sometimes'):
        result = 3
    elif(work_interfere=='Often'):
        result = 4
    return(result)
df_pred['work_interfere'] = df_pred['work_interfere'].apply(transform)











model = joblib.load('mh_rf_model.pkl')
prediction = model.predict(df_pred)

if st.button('Predict'):

    if(prediction[0]==0):
        st.write('<p class="big-font">You are not showing clear signs of mental health disorders.</p>',unsafe_allow_html=True)

    else:
        st.write('<p class="big-font">You are likely to have mental health disorders.Medical attention is advised.</p>',unsafe_allow_html=True)


