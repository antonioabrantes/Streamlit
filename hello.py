import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

from pathlib import Path
import google.generativeai as genai
import numpy as np
import os
import sys
import time

 
st.write(""" Teste comparativo de IA generativa """)

chart_selection = st.radio("Selecione o gráfico:", ("ChatCGP/OpenAI", "Gemini/Google"))

# Renderiza o gráfico selecionado com base na seleção do usuário

if chart_selection == "ChatCGP/OpenAI":
    st.write("ChatCGP/OpenAI")
elif chart_selection == "Gemini/Google":
    st.write("Gemini/Google ")
    
    api_key = os.getenv("GEMINI_API_KEY")
    #st.write(api_key)
    genai.configure(api_key=api_key)

    # Instrução do sistema para o modelo generativo
    system_instruction = f"""
    voce é um site de dúvidas frequentes da universidade federal do estado do rio de janeiro, e gostaria que, a partir das perguntas e respostas abaixo, quando ou fizer novamente a pergunta, responda de acordo e exatamente como as respostas fornecidas abaixo, sem inventar nada: Perguntas Frequentes por Brenda Cristine de Jesus Miranda — última modificação 29/02/2024 19h30 
    Qual tipo de documento será produzido no SEI da UNIRIO? O tipo de documento principal que será produzido no SEI da UNIRIO será o processo administrativo e todos os demais tipos documentais que precisam compor um processo administrativo produzido na universidade. O SEI da UNIRIO não produzirá documentos isoladamente, apenas aqueles que forem necessários para a instrução do processo administrativo eletrônico da Universidade. Como pesquisar um processo? Para pesquisar um processo, clique no campo “Menu” e digite o que deseja encontrar em “Pesquisa”. Se já possui o número do processo que deseja buscar sua localização, pode digitá-lo no campo “Nº SEI” da guia de pesquisa aberta. O que é um documento interno e externo no SEI? Documento interno é todo documento criado no próprio sistema, enquanto o documento externo é todo aquele que se precisa fazer o upload para o sistema. O documento externo pode ser nato-digital ou digitalizado. O documento externo nato digital é aquele que foi produzido e assinado eletronicamente, enquanto o digitalizado é aquele cujo PDF/A foi produzido a partir de um documento em papel. Como deverá ser a digitalização para o SEI? Todos os usuários que utilizarem o SEI direta ou indiretamente deverão produzir documentos digitalizados, conforme os padrões estabelecidos no Manual da ENAP: Cor monocromático, resolução com 300 dpi e opção de reconhecimento de texto (OCR) ativada, privilegiando o formato PDF. No entanto, se o original estiver em excelentes condições, o documento poderá ser digitalizado com 200 a 240 dpi. As notas fiscais, fotos e documentos coloridos em geral devem ser digitalizados com pelo menos 100 dpi. Sendo que, para os manuscritos, documentos impressos em fontes desalinhadas e/ou muito pequenas, para os documentos muito complexos (compostos por diagrama, tabelas e textos, fotografias), deverão ser ajustados para parâmetros específicos, a fim de se conseguir a melhor qualidade possível, de acordo com o Manual em referência. Como criar um documento interno? Em controle de processos, clique no processo desejado para adicionar o documento. Após, clique no ícone “Incluir Documento”. Os tipos de documentos apresentados na tela são os que a unidade já usou. Caso deseje outros documentos clique no ícone com o sinal de soma “+” e escolha o documento desejado. Preencha os campos conforme indica o “Guia do usuário SEI UNIRIO”. link: http://www.unirio.br/sei/arquivos/UsuariointernoManualdeusodoSEI.pdf Como criar um documento externo? Apenas documentos externos no formato PDF/A PESQUISÁVEL (OCR) são permitidos no SEI UNIRIO. Em controle de processos, clique no processo desejado para adicionar o documento. Após, clique no ícone “Incluir Documento”. Os tipos de documentos apresentados na tela são os que a unidade já usou. Clique em “Externo”. Preencha os campos conforme indica o "Guia do usuário SEI UNIRIO". Link: http://www.unirio.br/sei/arquivos/UsuariointernoManualdeusodoSEI.pdf Como classificar um documento que está sendo incorporado ao processo criado no SEI seja como documento interno ou externo? O usuário não precisará se preocupar com a classificação, pois o mesmo poderá passar o mouse sobre o número do processo que aparecerá o assunto que o mesmo foi classificado, este será o assunto para todos os documentos arrolados no processo desde a sua autuação. Observa-se que no momento da autuação do processo o assunto e o código de Classificação da Tabela de Temporalidade e Destinação de Documentos de Atividade-Meio (2020) ou Fim (2011) a serem utilizados no SEI serão os vigentes. Como fazer o “Texto Padrão”? No menu da tela, à sua esquerda, clique em “Textos Padrão”. Clique no botão “Novo”. No campo “nome”, digite o nome que identifica o texto. No campo "Descrição", detalhe a função desse texto. Clique na área do texto e digite o conteúdo. Clique no botão “Salvar”. A lista de “Textos Padrão” cadastrados na unidade aparecerão em ordem alfabética. Como usar um “Texto Padrão”? Em controle de processos, clique no processo desejado para adicionar documento com “Texto Padrão”. Após, clique no ícone “Incluir Documento”. Os tipos de documentos apresentados na tela são os que a unidade já usou. Caso deseje outros documentos clique no ícone com o sinal de soma (“+”) e escolha o tipo documental interno desejado. No campo “Texto Inicial” clique em “Texto Padrão”. Digite no campo ou clique na lupa para pesquisar o “Texto Padrão” desejado. Após achar o “Texto Padrão” desejado, clique nele e depois no botão “Transportar”. Preencha os campos conforme indica o “Guia do usuário SEI UNIRIO”. link: http://www.unirio.br/sei/arquivos/UsuariointernoManualdeusodoSEI.pdf Como criar um bloco de assinatura? No menu da tela à sua esquerda, clique em “Blocos” e depois em “Assinatura”. Clique no botão “Novo”. Após, descreva a função deste bloco. Ele precisa estar vinculado a um grupo. Escolha na lupa ou digite as unidades para disponibilização, após clique em “Salvar”. Como disponibilizar o documento do processo para um bloco de assinatura? Em controle de processos, clique no processo desejado para adicionar o bloco de assinatura. Após clicar no documento desejado, clique no ícone “Incluir em Bloco de Assinatura”. Na nova tela que se abrirá, opte pelo bloco de assinatura já cadastrado em “Bloco” e depois em “Incluir e Disponibilizar”. Caso ainda não tenha previamente constituído um bloco de assinatura, siga as seguintes operações: Clique no botão “Novo Bloco”. Após, descreva a função deste bloco. Pois, qualquer bloco de assinatura precisa estar vinculado a um grupo. Em seguida escolha a(s) unidade(s) a que este bloco estará recolhendo assinaturas quando for gerado, isso pode ser realizado por meio do ícone de lupa ou digitando as unidades para disponibilização, após este passo é só “Salvar”. Constituído o novo bloco de assinaturas desejado, clique no(s) documento(s) que deseja disponibilizar. Após clique no botão “Incluir e Disponibilizar”. Em ambos os casos aparecerá junto ao número de processo um ícone de alerta de que um ou mais documentos foram assinados para quem gerou o bloco de assinatura. Observa-se que o sistema não emite nenhum alerta para quem recebe o bloco, assim a unidade que deverá assinar o bloco de assinatura precisará ser avisada por outros meios de comunicação e acessar no “Menu”, o botão “Blocos” do tipo “Assinatura” para verificar se há pendências de assinaturas em blocos criadas para a respectiva unidade. Enquanto não assinarem o documento disponibilizado no bloco de assinatura, o processo ficará aberto no meu setor? Sim, enquanto o documento estiver pendente de assinatura o processo permanecerá aberto no setor de origem. Posso cancelar documento? Um documento pode ser cancelado toda vez que for constatado o erro de produção documental após a tramitação/envio de um processo para outra unidade. Pois, após o envio do processo para outra unidade, o ícone “Excluir” não constará mais para o usuário, apenas o ícone “Cancelar Documento”, com a devida justificativa a ser informada. Observando que, diferentemente da exclusão, o documento cancelado ainda constará na árvore do processo, mas não estará apto para a leitura. Posso excluir documento? Só se pode excluir um documento caso o mesmo não tenha sido tramitado. Nesta hipótese é só clicar no documento que deseja excluir e clicar no ícone com o desenho de uma lixeira vermelha e “Excluir”. Observa-se que qualquer modificação nos documentos, seja em suas versões ou a sua exclusão, são captados pelo sistema, por isso recomendamos o bom uso das ferramentas disponibilizadas no Sei, seja na sua edição ou tramitação. Como será a autuação de processo no SEI? A autuação de processo no Sistema Eletrônico de Informações (SEI) da UNIRIO será realizada somente por suas unidades de protocolo a partir da inclusão paulatina dos assuntos e dos Códigos de Classificação de Documentos (CCD) das Tabelas de Temporalidade e Destinação de Documentos (TTDD) de Atividade-Meio e Fim, tendo em vista as seguintes rotinas: Recebimento da “Solicitação de Autuação de Processo” em PDF/A, devidamente preenchido, conforme a Instrução Normativa AC/UNIRIO nº 02/2021, que dispõe sobre as solicitações de autuação de processos e, com isso, faz constar nas solicitações os seguintes campos: -Nome do Interessado; -Código e Assunto da Tabelas de Temporalidade e Destinação de Documentos de Atividade-Meio (2020) e Fim (2011) em vigência; -Descrição do assunto; -Destinatário do processo; Atenção: Os documentos digitalizados no SEI deverão estar em PDF/A, com Optical Character Recognition (OCR) para tornar o arquivo pesquisável. Já os documentos nato-digitais poderão ser assinados digitalmente pelo Gov.br ou outro sistema de assinatura eletrônica válida. Observando que os documentos enviados para autuação por meio do correio eletrônico deverão conter o seguinte título do assunto: “Autuação de Processo SEI. sigla da unidade solicitante”. Como envio processo no SEI? Clicar no ícone “Enviar Processo”; Na tela aberta “Enviar Processo” verificar o número e o tipo de processo no campo “Processos”; Buscar em “Unidades” por meio da lupa, à direita, a unidade destinatária já inclusa no SEI; Escolher a opção “Enviar e-mail de notificação”, caso queira notificar a unidade para qual está tramitando o processo; “Enviar”, para completar a ação de tramitação de processo com sucesso. Como enviar processo para arquivamento? Trata-se da operacionalização da conclusão de processos e de seu arquivamento no SEI que implica os seguintes passos: Conclusão do processo pela unidade competente, por meio da inclusão do documento interno: “Despacho de Arquivamento de Processo” (que conterá o pedido de arquivamento eletrônico do processo); Tramitar o processo para a unidade de protocolo responsável por sua abertura e/ou gestão; Após o recebimento do processo pela unidade protocolizadora, a mesma deverá tramitar para a unidade de arquivamento para processos do SEI para “Concluir Processo” no SEI. Atenção: Após a conclusão do processo, o mesmo só poderá ser pesquisado na unidade de arquivamento. A pesquisa poderá ser realizada da seguinte forma: Login e senha no SEI/ “Menu”/ “Pesquisa”/ Preencher os campos para filtragem/ selecionar o processo para leitura ou desarquivamento dos trâmites processuais. Para o desarquivamento do processo será necessário ainda clicar no primeiro documento do processo e clicar em “Reabrir Processo”. 18. Como solicitar a migração de processo físico do SIE para o SEI? 1) Verifique se a tipologia do processo já foi inserida no Sistema em: https://docs.google.com/spreadsheets/d/1TbkgeVmSdaHMN0zW18BC1AWO9GsLC78U8xwC89ElTcc/edit?usp=drivesdk ; 2) Digitalize o processo físico em PDF por volume (até 400 imagens) e nomeie o processo como o ex.: processo_23102000000202312_vu (volume único, v1, v2, etc); 3) Preencha e assine o ofício de solicitação disponível em: https://docs.google.com/document/d/1T4RDKEKEzYB8AUvVroN5lMv0BIgebmme/edit; 4) Envie o processo digitalizado + ofício para o e-mail sei@unirio.br; 5) Após realizado o procedimento, a equipe SEI enviará um Termo de Encerramento de Trâmite Físico que deverá ser inserido na última página do processo físico e o mesmo deverá ser encaminhado para o Arquivo Setorial ou Arquivo Central via malote para arquivamento definitivo, conforme orientação posterior via e-mail.  
    """

    #model = genai.GenerativeModel("gemini-pro") # teste
    #response = model.generate_content("O que é uma patente ?")
    #st.write(response.text)
    #sys.exit(0)

    # Inicializa o modelo generativo
    model = genai.GenerativeModel(
      model_name="gemini-1.5-pro-latest",
      system_instruction=system_instruction
    )

    # Mensagem inicial do modelo
    initial_model_message = "Olá, eu sou Sophia, um assistente virtual que te ajuda a tirar suas dúvidas sobre o SEI. Faça sua pergunta:"

    # Inicializa a conversa do assistente virtual
    if "chat_encontra" not in st.session_state:
        st.session_state.chat_encontra = model.start_chat(history=[{'role':'model', 'parts': [initial_model_message]}])

    # Título da página
    st.title('BatePapo 💬')

    # Introdução do assistente virtual
    st.write("A Assistente Virtual Sophia está aqui para te ajudar a tirar suas dúvidas sobre o SEI. Vamos começar?")

    # Exibe o histórico de conversa
    for i, message in enumerate(st.session_state.chat_encontra.history):
      if message.role == "user":
        with st.chat_message("user"):
          st.markdown(message.parts[0].text)
      else:
        with st.chat_message("assistant"):
          st.markdown(message.parts[0].text)

    # Entrada do usuário
    user_query = st.chat_input('Você pode digitar sua resposta aqui:')

    # Processamento da entrada do usuário e resposta do assistente
    if user_query is not None and user_query != '':
        with st.chat_message("user"):
          st.markdown(user_query)
        with st.chat_message("assistant"):
            ai_query = st.session_state.chat_encontra.send_message(user_query).text
            st.markdown(ai_query)
