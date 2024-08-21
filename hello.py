import os
from dotenv import load_dotenv
#from langchain_openai import ChatOpenAI
#from langchain_core.output_parsers import StrOutputParser
#from langchain_core.prompts import ChatPromptTemplate
#from langchain.chains import ConversationChain

import streamlit as st

# Captura os parâmetros da URL
# http://localhost:8501/?param1=valor1&param2=valor2
query_params = st.experimental_get_query_params()

# Acessa os valores dos parâmetros
param1 = query_params.get('param1', [''])[0]
param2 = query_params.get('param2', [''])[0]

# Exibir os valores no Streamlit
st.write(f"Valor de param1: {param1}")
st.write(f"Valor de param2: {param2}")

texto = "<xml>Testando</xml>"
write open('teste.txt','w',encoding='utf-8') as arquivo:
    arquivo.write(texto)