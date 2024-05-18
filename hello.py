import streamlit as st
import pandas as pd
import requests
 
st.write("""
# My first app
Olá mundo* 
""")
# df = pd.read_csv("my_data.csv")
# st.line_chart(df)

url = "http://www.cientistaspatentes.com.br/apiphp/patents/query/?q={%22mysql_query%22:%22divisao,count(*)%20FROM%20arquivados%20where%20despacho=%2715.23%27%20and%20year(data)%3E=2000%20group%20by%20divisao%20order%20by%20count(*)%20desc%22}"
# Definindo cabeçalhos para a requisição
headers = {
    "Accept": "application/json"
}

try:
    # Requisição para obter os dados JSON
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verificar se a requisição foi bem-sucedida

    # Tentar decodificar o JSON
    data = response.json()

    # Carregar os dados JSON em um DataFrame
    df = pd.DataFrame(data['patents'])

    # Verificar e converter a coluna 'count' para inteiro
    df['count'] = pd.to_numeric(df['count'], errors='coerce')

    # Mostrar o DataFrame
    st.write("## Patents Data", df)

    # Exibir o gráfico de linhas
    st.line_chart(df.set_index('divisao')['count'])

except requests.exceptions.HTTPError as http_err:
    st.error(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    st.error(f"Error occurred during request: {req_err}")
except ValueError as json_err:
    st.error(f"JSON decode error: {json_err}")
except Exception as err:
    st.error(f"An unexpected error occurred: {err}")