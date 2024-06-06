import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
 
st.write(""" Teste comparativo de IA generativa """)

chart_selection = st.radio("Selecione o gráfico:", ("ChatCGP/OpenAI", "Gemini/Google"))

# Renderiza o gráfico selecionado com base na seleção do usuário

if chart_selection == "ChatCGP/OpenAI":
    st.write("ChatCGP/OpenAI")
elif chart_selection == "Gemini/Google":
    st.write("Gemini/Google ")
