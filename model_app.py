import joblib
import streamlit as st

@st.cache_resource
def load_model():
    return joblib.load("regression.joblib")

model = load_model()

taille = st.number_input("Taille (m²)", min_value=10.0, max_value=1000.0, value=80.0, step=5.0)
chambres = st.number_input("Nombre de chambres", min_value=0, max_value=20, value=2, step=1)
jardin = st.number_input("Jardin (0 = non, 1 = oui)", min_value=0, max_value=1, value=0, step=1)

if st.button("Prédire"):
    prediction = model.predict([[taille, chambres, jardin]])
    st.write(f"Prix estimé : {prediction[0]:,.0f} €")