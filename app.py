import streamlit as st
import pickle
import numpy as np
st.markdown("This is an app to check whether a person can donate blood or not as pathologist do not want a smoker to donate blood. So firstly he asks hemoglobin, and B.P. If hemoglobin is greter than 16 and B.P is greter than 150/100. That person cannot give the blood ")
md=pickle.load(open("md.pkl",'rb'))

#gender=st.text_input("Gender(0 or 1) ")
hemoglobin=st.text_input("Enter the hemoglobin")
systolic=st.text_input("Enter the systolic")
relaxation=st.text_input("Enter the relaxation")

#gender=int(gender)
systolic=float(systolic)
relaxation=float(relaxation)
hemoglobin = float(hemoglobin)
if hemoglobin<16.0 and systolic<150.0 and relaxation<90.0:  
    if st.button("Predict"):    
    
        st.write("The person can give the blood")
else    :
        gender=st.text_input("Gender (0 or 1)")
        tartar=st.text_input("Tartar presence(0 or 1) ")
        dental_caries=st.text_input("dental caries(0 or 1) ")
        Urine_Protein=st.text_input("Enter the Urine Protein")
        height=st.text_input("Enter the height(cm)")
        hearing=st.text_input("Enter the hearing(right)")
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
        if st.button("Predict"):
            
    
                input_data=[tartar,dental_caries,hemoglobin,Urine_protein,height,hearing,relaxation,gtp,triglyseride,serum_creatnine,systolic,gender]
                input_data_array=np.asarray(input_data,dtype=np.float64)

                input_data_reshaped=input_data_array.reshape(1,-1)
                prediction=md.predict(input_data_reshaped)
                if(prediction==1):
                    st.write("The Person cannot give blood")
                else:
                    st.write("The Person can give blood")
      