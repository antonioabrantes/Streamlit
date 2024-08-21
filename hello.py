from flask import Flask
import os
from dotenv import load_dotenv
#from langchain_openai import ChatOpenAI
#from langchain_core.output_parsers import StrOutputParser
#from langchain_core.prompts import ChatPromptTemplate
#from langchain.chains import ConversationChain


app = Flask(__name__)

@app.route('/')
def homepage():
  return 'Esta é a homepage do site'

@app.route('/contatos')
def contatos():
  return 'Esta é a lista de contatos'

app.run(host='0.0.0.0')