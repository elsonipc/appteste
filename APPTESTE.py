import streamlit as st

# Título do app
st.title("App Simples com Streamlit")

# Campo de texto para inserir o nome
nome = st.text_input("Digite seu nome:")

# Exibe uma saudação quando o botão é pressionado
if st.button("Clique para saudar"):
    if nome:
        st.write(f"Olá, {nome}! Bem-vindo ao Streamlit!")
    else:
        st.write("Olá! Por favor, insira seu nome.")
