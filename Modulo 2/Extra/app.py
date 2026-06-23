
import streamlit as st

st.subheader('RH AÇOUGUE - Sistema de Cadastro de Funcionários')

st.sidebar.image('ney.png')
st.sidebar.image('ney1.png')

nome = st.text_input('Digite o nome do Funcionário👨‍💼')
idade = st.number_input('Digite a idade do Funcionário📏', min_value=0, max_value=120)
email = st.text_input('Digite o e-mail do Funcionário✉️')
salario = st.number_input('Digite o salário do Funcionário💵💰', min_value=0.0, format="%.2f")
cargo = st.text_input('Digite o cargo do Funcionário💼')

if st.button('Cadastrar'):
    if nome and email and cargo:
        st.balloons()
        st.success(f'Funcionário {nome}, cargo {cargo}, e-mail {email}, cadastrado com salário R$ {salario} por mes')
        st.image('https://thispersondoesnotexist.com/')
    else:
        st.error('Preencha todos os campos obrigatórios!')
        