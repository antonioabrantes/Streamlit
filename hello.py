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
p1 = query_params.get('param1', [''])[0]
p2 = query_params.get('param2', [''])[0]

# Exibir os valores no Streamlit
# st.write(f"Valor de param1: {p1}")
# st.write(f"Valor de param2: {p2}")

import streamlit as st
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    return jsonify({"param1": nome, "param2": idade})

if __name__ == '__main__':
    app.run(port=5000)