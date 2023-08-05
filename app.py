import streamlit as st
import pickle
import numpy as np

md=pickle.load(open("md.pkl",'rb'))
gender=st.text_input("Gender(0 or 1) ")
tartar=st.text_input("Tartar presence(0 or 1) ")
dental_caries=st.text_input("dental caries(0 or 1) ")
hemoglobin=st.text_input("Enter the hemoglobin")
Urine_Protein=st.text_input("Enter the Urine Protein")
height=st.text_input("Enter the height(cm)")
hearing=st.text_input("Enter the hearing(right)")
systolic=st.text_input("Enter the systolic")
relaxation=st.text_input("Enter the relaxation")
gtp=st.text_input("Enter the gtp")
triglyseride=st.text_input("Enter the triglyseride")
serum_creatnine=st.text_input("Enter the serun creatnine")  

tartar = int(tartar)

systolic=float(systolic)
hemoglobin = float(hemoglobin)
Urine_protein = float(Urine_Protein)
height = float(height)
hearing = float(hearing)
relaxation = float(relaxation)
gtp = float(gtp)
triglyseride = float(triglyseride)
serum_creatnine=float(serum_creatnine)
if hemoglobin>16 and systolic>150 and relaxation>100:
    if st.button("Predict"):
        input_data=[tartar,dental_caries,hemoglobin,Urine_protein,height,hearing,relaxation,gtp,triglyseride,serum_creatnine,systolic,gender]
        input_data_array=np.asarray(input_data,dtype=np.float64)

        input_data_reshaped=input_data_array.reshape(1,-1)
        prediction=md.predict(input_data_reshaped)
        if(prediction==1):
            st.write("The Person do smoke!")
        else:
            st.write("The Person do not smoke")
        
      