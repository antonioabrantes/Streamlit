import streamlit as st
import pandas as pd
import requests
 
st.write("""
# My first app
Olá mundo* 
""")
 
url = "http://www.cientistaspatentes.com.br/apiphp/patents/query/?q={%22mysql_query%22:%22divisao,count(*)%20FROM%20arquivados%20where%20despacho=%2715.23%27%20and%20year(data)%3E=2000%20group%20by%20divisao%20order%20by%20count(*)%20desc%22}"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data['patents'])
# Verificar e converter a coluna 'count' para inteiro
df['count'] = pd.to_numeric(df['count'], errors='coerce')


# df = pd.read_csv("my_data.csv")
# st.line_chart(df)

# Mostrar o DataFrame
st.write("15.23", df)

# Exibir o gráfico de linhas
st.line_chart(df.set_index('divisao')['count'])
