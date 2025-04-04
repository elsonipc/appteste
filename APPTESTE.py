import streamlit as st

# T�tulo do app
st.title("App Simples com Streamlit")

# Campo de texto para inserir o nome
nome = st.text_input("Digite seu nome:")

# Exibe uma sauda��o quando o bot�o � pressionado
if st.button("Clique para saudar"):
    if nome:
        st.write(f"Ol�, {nome}! Bem-vindo ao Streamlit!")
    else:
        st.write("Ol�! Por favor, insira seu nome.")
