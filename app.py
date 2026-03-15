import streamlit as st
import os
import json
import google.generativeai as genai

# CONFIGURAR API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="DocSwift Jurídico", layout="wide")

st.title("⚖️ DocSwift IA Jurídica")

# ---------------------------------------------------
# CARREGAR LEGISLAÇÃO
# ---------------------------------------------------

@st.cache_data
def carregar_legislacao():

    pasta = "database/legislacao"
    textos = []

    for arquivo in os.listdir(pasta):

        with open(os.path.join(pasta, arquivo), "r", encoding="utf-8") as f:
            textos.append(f.read())

    return "\n".join(textos)


# ---------------------------------------------------
# CARREGAR JURISPRUDÊNCIA
# ---------------------------------------------------

@st.cache_data
def carregar_jurisprudencia():

    base = []

    with open("database/jurisprudencia/stf.json", encoding="utf-8") as f:
        base.extend(json.load(f))

    with open("database/jurisprudencia/stj.json", encoding="utf-8") as f:
        base.extend(json.load(f))

    return base


# ---------------------------------------------------
# BUSCAR TRECHOS RELEVANTES
# ---------------------------------------------------

def buscar_contexto(texto, pergunta):

    palavras = pergunta.lower().split()

    resultados = []

    for linha in texto.split("\n"):

        for palavra in palavras:

            if palavra in linha.lower():

                resultados.append(linha)

    return "\n".join(resultados[:30])


def buscar_jurisprudencia(base, pergunta):

    resultados = []

    for item in base:

        if item["tema"].lower() in pergunta.lower():

            resultados.append(
                f'{item["tribunal"]} - {item["tese"]} ({item["fonte"]})'
            )

    return "\n".join(resultados)


# ---------------------------------------------------
# INTERFACE
# ---------------------------------------------------

pergunta = st.text_area("Digite sua pergunta jurídica:")

if st.button("Analisar"):

    leis = carregar_legislacao()
    juris = carregar_jurisprudencia()

    contexto_legal = buscar_contexto(leis, pergunta)
    contexto_juris = buscar_jurisprudencia(juris, pergunta)

    prompt = f"""
    Você é um jurista especialista em direito brasileiro.

    LEGISLAÇÃO RELEVANTE:
    {contexto_legal}

    JURISPRUDÊNCIA:
    {contexto_juris}

    PERGUNTA:
    {pergunta}

    Elabore uma análise jurídica fundamentada.
    """

    resposta = model.generate_content(prompt)

    st.subheader("Parecer Jurídico")
    st.write(resposta.text)
