import streamlit as st
#Titulo de la Aplicacion
st.title("Bienvenido Oigame a mi aplicacion")
#SOlicitar nombre del usuario
nombre = st.text_input("Por favor, ingresa tu nombre:")
#Mostrar el saludo si el usuario ingresa su nombre
if nombre:
    st.write(f"Hola, (nombre)Bienvenido a esta aplicacion")