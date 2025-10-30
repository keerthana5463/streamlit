import streamlit as st
import pickle
import numpy as np

st.title("Laptop Price Prediction")
st.text("This app is created by using ML model developed in one of our previous sessions")
import pickle
ml_model=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))


company=st.selectbox("Manufacturer of the laptop",df['Company'].unique(),index=4)
typename=st.selectbox("Type of the laptop",df['TypeName'].unique(),index=1)
cpu=st.selectbox("Processor on the laptop",df['Cpu'].unique())
ram=st.radio('RAM(in GB)',[4,8,12,16,24,32,64],index=1,horizontal=True)
gpu=st.selectbox("Graphics Card on the laptop",df['Gpu'].unique(),index=1)
os=st.selectbox("Operating system on the laptop",df['OpSys'].unique(),index=2)
weight=st.slider("Weight of the laptop(in kg)",min_value=0.8,max_value=4.5,value=2.0,step=0.1)
ips=st.radio("Does the laptop have an IPS display?",["Yes","No"],index=1,horizontal=True)
touchscreen=st.radio("Does the laptop have a touchscreen?",["Yes","No"],index=1,horizontal=True)
cpu_speed=st.slider("What is the clock speed of the processor(in GHz)?",min_value=0.8,max_value=4.5,step=0.1,value=2.2)
hdd=st.radio("HDD size(in GB). Select 0 if system only has SSD storage",[0,512,1024,2048],horizontal=True)
ssd=st.radio("SSD size(in GB). Select 0 if system only has HDD storage",[0,128,256,512,1024],index=3,horizontal=True)
ppi=st.slider("What is the PPI(pixel density) of the laptop?",min_value=75,max_value=400,step=5,value=150)

if st.button("PREDICT PRICE"):
    if ips=="Yes":
        ips=1
    else:
        ips=0
    if touchscreen == 'Yes':
        touchscreen=1
    else:
        touchscreen=0
    query=np.array([[company, typename,cpu,ram, gpu,os, weight, ips, touchscreen, cpu_speed, hdd, ssd, ppi]])
    op=ml_model.predict(query)
    st.subheader("The estimated price of the laptop with the above mentioned specifications is ₹"+str(int(round(op[0],-2))))
