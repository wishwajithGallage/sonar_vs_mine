# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


# loading the saved models

sonar_model = pickle.load(open('E:\ml projects\Classification Machine Learning Projects 6\SONAR Rock vs Mine Prediction with Python\web\rock_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Sonar_Rock_vs_Mine_Pediction',
                          
                          ['Sonar_Rock_vs_Mine_Pediction'],
                          icons=['activity'],
                          default_index=0)
    
    

        
    
    

# Parkinson's Prediction Page
if (selected == "Sonar_Rock_vs_Mine_Pediction"):
    
    # page title
    st.title("Sonar_Rock_vs_Mine_Pediction using ML")
    
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)  
    
    with col1:
        v0 = st.text_input('0')
        
    with col2:
        V1 = st.text_input('1')
        
    with col3:
        V2 = st.text_input('2')
        
    with col4:
        V3 = st.text_input('3')
        
    with col5:
        V4 = st.text_input('4')
        
    with col6:
        V5 = st.text_input('5')
        
    with col7:
        V6 = st.text_input('6')
        
    with col8:
        V7 = st.text_input('7')
        
    with col9:
        V8 = st.text_input('8')
        
    with col10:
        V9 = st.text_input('9')
        
    with col1:
        V10 = st.text_input('10')
        
    with col2:
        V11 = st.text_input('11')
        
    with col3:
        V12 = st.text_input('12')
        
    with col4:
        V13 = st.text_input('13')
        
    with col5:
        V14 = st.text_input('14')
        
    with col6:
        V15 = st.text_input('15')
        
    with col7:
        V16 = st.text_input('16')
        
    with col8:
        V17 = st.text_input('17')
        
    with col9:
        V18 = st.text_input('18')
        
    with col10:
        V19 = st.text_input('19')
        
    with col1:
        V20 = st.text_input('20')
        
    with col2:
        V21 = st.text_input('21')
        
    with col3:
        V22 = st.text_input('22')
        
    with col4:
        V23 = st.text_input('23')
        
    with col5:
        V24 = st.text_input('24')
        
    with col6:
        V25 = st.text_input('25')
        
    with col7:
        V26 = st.text_input('26')
        
    with col8:
        V27 = st.text_input('27')
        
    with col9:
        V28 = st.text_input('28')
        
    with col10:
        v29 = st.text_input('29')
        
    with col1:
        V30 = st.text_input('30')
        
    with col2:
        V31 = st.text_input('31')
        
    with col3:
        V32 = st.text_input('32')
        
    with col4:
        V33 = st.text_input('33')
        
    with col5:
        V34 = st.text_input('34')
        
    with col6:
        V35 = st.text_input('35')
        
    with col7:
        V36 = st.text_input('36')
        
    with col8:
        V37 = st.text_input('37')
        
    with col9:
        V38 = st.text_input('38')
        
    with col10:
        V39 = st.text_input('39')
        
    with col1:
        V40 = st.text_input('40')
        
    with col2:
        V41 = st.text_input('41')
        
    with col3:
        V42 = st.text_input('42')
        
    with col4:
        V43 = st.text_input('43')
        
    with col5:
        V44 = st.text_input('44')
        
    with col6:
        V45 = st.text_input('45')
        
    with col7:
        V46 = st.text_input('46')
        
    with col8:
        V47 = st.text_input('47')
        
    with col9:
        V48 = st.text_input('48')
        
    with col10:
        V49 = st.text_input('49')
        
    with col1:
        V50 = st.text_input('50')
        
    with col2:
        V51 = st.text_input('51')
        
    with col3:
        V52 = st.text_input('52')
        
    with col4:
        V53 = st.text_input('53')
        
    with col5:
        V54 = st.text_input('54')
        
    with col6:
        V55 = st.text_input('55')
        
    with col7:
        V56 = st.text_input('56')
        
    with col8:
        V57 = st.text_input('57')
    
    with col9:
        v58 = st.text_input('58')
        
    with col10:
        V59 = st.text_input('59')
        
    
        
    
    
    # code for Prediction
    Sonar_ = ''
    
    # creating a button for Prediction    
    if st.button("Sonar_vs_Mine_Test_Result"):
        # Assuming Time, V1 to V28, and Amount are variables with proper numeric values
       # input_data = np.array([[Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]], dtype=float)
        #input_data = [v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32,v33,v34,v35,v36,v37,v38,v39,v40,v41,v42,v43,v44,v45,v46,v47,v48,v49,v50,v51,v52,v53,v54,v55,v56,v57,v58,v59]
        #reshaped_data = np.array(input_data).reshape(1, -1)
        #Sonar_Rock_vs_Mine_Pediction = sonar_model.predict(reshaped_data)
        # Now use this input_data for prediction
        #Sonar_Rock_vs_Mine_Pediction = sonar_model.predict(input_data)
        Sonar_Rock_vs_Mine_Pediction = sonar_model.predict([[v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32,v33,v34,v35,v36,v37,v38,v39,v40,v41,v42,v43,v44,v45,v46,v47,v48,v49,v50,v51,v52,v53,v54,v55,v56,v57,v58,v59]])                          
        
        if (Sonar_Rock_vs_Mine_Pediction[0] == R):
          Sonar_ = "The object is a Rock"
        else:
         Sonar_ = "The object is a mine"
        
    st.success(Sonar_)






