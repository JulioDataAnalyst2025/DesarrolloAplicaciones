Import streaamlit as st

st.title("Clasificacion de puntajes")
def Clasificarpuntaje(Puntaje):
    if Puntaje >= 85:
        return "Excelente"
    elif Puntaje >= 70:
        return "Bueno"
    else
        return "Necesita mejorar"
    
#Interfaz en Streamlit
st.title ("Clasificacion de puntajes")
st.write("Ingrese un puntaje y el sistema lo clasificara")

#Entrada de usuario
puntaje=st.number_input("Ingrese el puntaje",min_value=0,max_value=100,step=1)

#Boton para clasificar
if st.button("Clasificar"):
    resultado=Clasificarpuntaje(Puntaje)
    st.success(f"El puntaje{Puntaje} es clasificado como:{resultado}")










