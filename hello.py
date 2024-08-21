import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import requests

def conectar_url(url,return_json=False):
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        if return_json:
            data = response.json()
            json_data = json.dumps(data, indent=4)
            return(json_data)
        else:
            return response.text
    else:
        return(f"Erro: {response.status_code}")

diretorio_corrente = os.getcwd() 
st.write(f"O diretório corrente é: {diretorio_corrente}")
txt_file = "teste.txt"
texto = "testando"
with open (txt_file,"w",encoding="utf-8") as arquivo:
   arquivo.write(texto)
if os.path.exists(txt_file):
    st.write(f"O arquivo {txt_file} existe")
else:
    st.write(f"O arquivo {txt_file} não existe")
arquivos_e_pastas = os.listdir()
arquivos = [f for f in arquivos_e_pastas if os.path.isfile(f)]
for arquivo in arquivos:
    st.write(arquivo)

# Captura os parâmetros da URL
# https://app-helloabrantes.streamlit.app/?numero=112012018157&doc=US20030065257
query_params = st.experimental_get_query_params()

# Acessa os valores dos parâmetros
numero = query_params.get('numero', [''])[0]
doc = query_params.get('doc', [''])[0]

# Exibir os valores no Streamlit
st.write(f"Numero: {numero}")
st.write(f"Doc: {doc}")

load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY2")
#st.write(open_api_key)

llm = ChatOpenAI(api_key=open_api_key)
out_parser = StrOutputParser()
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um assistente virtual."),
        ("user", "{user_input}"),
    ])

chain = prompt | llm | out_parser

# query = "Qual a capital do Brasil?"
# resposta = chain.invoke({"user_input":f"{query}"})
# st.write(resposta)

# Primeira etapa: obter resumo d documento em exame, uma vez que relatório descritivo não está disponível
# https://patents.google.com/patent/BR112012018157A2/pt?oq=BR112012018157
# numero = '112012018157'
url = f"https://patents.google.com/patent/BR{numero}A2/pt?oq=BR{numero}"
#data = conectar_url(url,return_json=False)
#st.write(data)
html = urlopen(url)
#print(html.read())
bs = BeautifulSoup(html.read(),'html.parser')
#print(bs.title)
nameList = bs.findAll("div", {"class":"abstract"})
texto_pedido = ''
for name in nameList:
    #st.write(name.getText())
    texto_pedido = name.getText()

# Segunda etapa: obter relatório de D1
# doc = 'US20030065257'
url = f"https://patents.google.com/patent/{doc}A1/en?oq={doc}"
data = conectar_url(url,return_json=False)
#print(data)
html = urlopen(url)
#print(html.read())
bs = BeautifulSoup(html.read(),'html.parser')
#print(bs.title)
nameList = bs.findAll("div", {"class":"abstract"})
resumo_D1 = ''
for name in nameList:
    #st.write(name.getText())
    resumo_D1 = name.getText()

texto_D1 = ''
nameList = bs.findAll("section", {"itemprop":"description"})
for name in nameList:
    #st.write(name.getText())
    texto_D1 = name.getText()

# Usar llm para fazer resumo de D1 e comparar com pedido em exame
query = f"resuma o documento D1: {texto_D1}"
resposta = chain.invoke({"user_input":f"{query}"})
st.write(f"Resumo D1 {doc}: {resposta}")
st.write("====")

query = f"resuma os problemas técnicos apontados em D1: {texto_D1}"
resposta = chain.invoke({"user_input":f"{query}"})
st.write(f"Problemas técnicos D1 {doc}: {resposta}")
st.write("====")

query = f"compare o pedido em exame: {texto_pedido} e o documento D1: {texto_D1} e aponte as diferenças"
resposta = chain.invoke({"user_input":f"{query}"})
st.write(f"Comparação: {resposta}")






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