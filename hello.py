import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!* 
""")
 
df = pd.read_csv("my_data.csv")
#st.line_chart(df)

#!pip install -q -U google_generativeai
import google.generativeai as genai
from google.colab import userdata

# https://aistudio.google.com/app/prompts/new_chat

GOOGLE_API_KEY="AIzaSyCDZ9F29gvkoZRoW7VfE9Xus34uALE424U"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("O que é uma patente ?")

print(response.text)

"""Listar os modelos disponíveis"""

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

# Set up the model gemini 1.5 não aceita ajuste se safety setting ou temperatura
generation_config = {
  "candidate_count" : 1,
  "temperature": 0.5, # aleatoridade das respostas , qunto mais perto de 1 mais criativo
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",generation_config=generation_config,safety_settings=safety_settings)

response = model.generate_content("O que é um modelo de utilidade ?")
print(response.text)