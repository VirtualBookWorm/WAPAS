import streamlit as st 
import pandas as pd
import plotly.express as px

@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df

@st.cache
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model			

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
		st.subheader("Predict sales")
		st.markdown('<a href="https://share.streamlit.io/virtualbookworm/wapas/main/predict.py">Proceed to predict sales</a>', unsafe_allow_html=True)
	else:
		st.error("Enter a valid Unique ID")

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.markdown('<p style="color:Aqua">&copy 2022 &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; WAPAS v1.5.0</p>', unsafe_allow_html=True)
st.markdown('<p style="color:Aqua">Designed &amp; developed by <a href="https://www.linkedin.com/in/aritra-ban3rjee/">Aritra Banerjee</a></p>', unsafe_allow_html=True)
