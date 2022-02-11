import streamlit as st 
import pandas as pd 
from PIL import Image

@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df

st.title("WAPAS")
st.subheader("Web Application to Predict & Analyse Sales")

st.text("")
st.text("")
st.text("")

UID = '1234'
ID = st.text_input("Enter your Unique ID: ", type='password')
if st.button("Authenticate"):
	if ID==UID:
		st.success("Successfully authenticated!")
		data = load_data("assets/database.csv")
		st.subheader("Exploratory Data")
		st.dataframe(data)
		with st.expander("See plotting..."):
			st.write("**Scatter plots as folloing**")
			img = Image.open('assets/images/plots.png')
			st.image(img)
			st.write("Therefore, **TV** adverts have the *highest* & **Newspaper** adverts have the *lowest* weight...")
		st.subheader("Predict sales")
		TV = st.slider('Spenditure on TV (million $)', 0, 300, 3)
		Newspaper = st.slider('Spenditure on Newspaper (million $)', 0, 200, 2)
		Radio = st.slider('Spenditure on Radio (million $)', 0, 100, 1)
		
		
	else:
		st.error("Enter a valid Unique ID")
		st.stop()
