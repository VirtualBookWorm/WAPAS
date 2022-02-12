import streamlit as st
import numpy as np
import joblib
import os

@st.cache
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

st.title("WAPAS")
st.subheader("Web Application to Predict & Analyse Sales")

st.text("")
st.text("")
st.text("")

st.markdown('<a href="https://share.streamlit.io/virtualbookworm/wapas/main/app.py">Go back to Homepage</a>', unsafe_allow_html=True)
	

st.text("")

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
		st.write("**Confidence:** Approx 60% accuracy is expected.")
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

st.markdown('<p style="color:Aqua">&copy 2022 &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; WAPAS v1.5.0</p>', unsafe_allow_html=True)
st.markdown('<p style="color:Aqua">Designed &amp; developed by <a href="https://www.linkedin.com/in/aritra-ban3rjee/">Aritra Banerjee</a></p>', unsafe_allow_html=True)

