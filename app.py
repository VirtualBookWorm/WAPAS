import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import joblib
import os

@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df

@st.cache
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model			

st.title("WAPAS")
st.header("Web Application to Predict & Analyse Sales")

st.text("")
st.text("")
st.text("")

st.write("<p style='color:Chocolate'><b>Note: User authentication is required to see the Database & Analytical reports!!</b> However, 'Sales prediction' can be accessed without password verification</p>", unsafe_allow_html=True)
UID = 'sample_1234'
ID = st.text_input("Enter your Unique ID: ", type='password')
if st.button("Authenticate"):
	if ID==UID:
		st.success("Successfully authenticated!")
		data = load_data("assets/advert_database.csv")
		st.subheader("Exploratory Data")
		st.dataframe(data)
		with st.expander("See detailed plotting..."):
			plot = px.scatter(data_frame=data, x='TV', y='Sales')
			st.plotly_chart(plot)
			plot = px.scatter(data_frame=data, x='Newspaper', y='Sales')
			st.plotly_chart(plot)
			plot = px.scatter(data_frame=data, x='Radio', y='Sales')
			st.plotly_chart(plot)
			st.write("***Note: Expenditure on X-axis in millions of $***")
			st.write("***Note: Sales amount on Y-axis in Billions of $***")
		with st.expander("See comparative analysis..."):
			st.image('assets/images/plots.png')
			st.write("Therefore, **TV** adverts have the *highest/most correlative* weight...")
	else:
		st.error("Enter a valid Unique ID")

st.text("")
st.text("")

st.subheader("Predict sales")
choice = st.selectbox("Select expenditure method...", ['None', 'Advertisement on TV', 'Advertisement on Radio', 'Advertisement on Newspaper (not recommended)'])
if choice=='None':
	pass
if choice=='Advertisement on TV':
	TV = st.slider("Advertisement expenditure on TV (in millions of $)", 0, 300, 1)
	if st.button("Predict"):
		sample = np.array([0,TV]).reshape(2)
		model = load_model("models/model.pkl")
		prediction = model.predict(sample)
		st.info("Generated report")
		st.write("Predicted sales: $ {:.2f}".format(prediction[0])," billion")
		st.write("**Confidence:** Approx 80% accuracy is expected. :sunglass:")
if choice=='Advertisement on Radio':
	Radio = st.slider("Advertisement expenditure on Radio", 0, 100, 1)
	if st.button("Predict"):
		sample = np.array([0,Radio]).reshape(2)
		model = load_model("models/model_Radio.pkl")
		prediction = model.predict(sample)

		st.info("Generated report")
		st.write("Predicted sales: $ {:.2f}".format(prediction[0])," billion")
		st.write("**Warning:** Approx 30% accuracy is expected (not reliable).")
if choice=='Advertisement on Newspaper (not recommended)':
	Newspaper = st.slider("Advertisement expenditure on Newspaper", 0, 200, 1)
	st.markdown('<p style="color:Red">Co-relation between Newspaper advertisement & sales is found to be negligible.</p>', unsafe_allow_html=True)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.markdown('<p style="color:Aqua">&copy 2022 &nbsp; WAPAS &nbsp;| &nbsp;&nbsp; Designed &amp; developed by <a href="https://www.linkedin.com/in/aritra-ban3rjee/">Aritra Banerjee</a></p>', unsafe_allow_html=True)
st.markdown('<p style="color:Aqua"><b>co-developers:</b> <a>Rounak Das</a>, <a>Sarat Sen</a>, <a>Ranadip Ghosh</a> &amp; <a>Indranuj Ganguly</a></p>', unsafe_allow_html=True)
