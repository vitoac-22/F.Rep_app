import streamlit as st

st.title("Mi primera aplicación en la Web")

nombre = st.text_input("¿Cuál es tu nombre?")

if nombre is not None:
    st.write(f"Bienvenido {nombre} a mi primera app Web")
