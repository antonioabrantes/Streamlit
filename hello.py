import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

# Captura os parâmetros da URL
# http://localhost:8501/?numero=valor1&doc=valor2
query_params = st.experimental_get_query_params()

# Acessa os valores dos parâmetros
numero = query_params.get('numero', [''])[0]
doc = query_params.get('doc', [''])[0]

# Exibir os valores no Streamlit
st.write(f"Numero: {numero}")
st.write(f"Doc: {doc}")

load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY2")
st.write(open_api_key)

llm = ChatOpenAI(api_key=open_api_key)
out_parser = StrOutputParser()
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um assistente virtual."),
        ("user", "{user_input}"),
    ])

chain = prompt | llm | out_parser

query = "Qual a capital do Brasil?"
#query = texto
resposta = chain.invoke({"user_input":f"{query}"})
st.write(resposta)


#import streamlit as st
#import json
#from flask import Flask, request, jsonify

#app = Flask(__name__)

#@app.route('/data', methods=['GET'])
#def get_data():
#    param1 = request.args.get('param1')
#    param2 = request.args.get('param2')
#    return jsonify({"param1": nome, "param2": idade})

#if __name__ == '__main__':
#    app.run(port=5000)