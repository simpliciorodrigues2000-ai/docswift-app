import streamlit as st
import google.generativeai as genai
import os
import json

# -------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -------------------------------------------------

st.set_page_config(
    page_title="DocSwift IA Jurídica",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ DocSwift - Assistente Jurídico com IA")

# -------------------------------------------------
# CONFIGURAR API
# -------------------------------------------------

api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ API KEY não encontrada no Streamlit Secrets.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

# -------------------------------------------------
# CARREGAR LEGISLAÇÃO
# -------------------------------------------------

@st.cache_resource
def carregar_legislacao():

    pasta = "database/legislacao"

    textos = []

    if not os.path.exists(pasta):
        return ""

    for arquivo in os.listdir(pasta):

        caminho = os.path.join(pasta, arquivo)

        with open(caminho, "r", encoding="utf-8") as f:
            textos.append(f.read())

    return "\n".join(textos)

# -------------------------------------------------
# CARREGAR JURISPRUDÊNCIA
# -------------------------------------------------

@st.cache_resource
def carregar_jurisprudencia():

    base = []

    try:
        with open("database/jurisprudencia/stf.json", encoding="utf-8") as f:
            base.extend(json.load(f))
    except:
        pass

    try:
        with open("database/jurisprudencia/stj.json", encoding="utf-8") as f:
            base.extend(json.load(f))
    except:
        pass

    return base

# -------------------------------------------------
# BUSCAR CONTEXTO LEGAL
# -------------------------------------------------

def buscar_contexto(texto, pergunta):

    palavras = pergunta.lower().split()

    resultados = []

    for linha in texto.split("\n"):

        for palavra in palavras:

            if palavra in linha.lower():
                resultados.append(linha)

    return "\n".join(resultados[:25])

# -------------------------------------------------
# BUSCAR JURISPRUDÊNCIA
# -------------------------------------------------

def buscar_jurisprudencia(base, pergunta):

    resultados = []

    for item in base:

        if item["tema"].lower() in pergunta.lower():

            resultados.append(
                f'{item["tribunal"]}: {item["tese"]} ({item["fonte"]})'
            )

    return "\n".join(resultados)

# -------------------------------------------------
# CARREGAR BASES
# -------------------------------------------------

leis = carregar_legislacao()
juris = carregar_jurisprudencia()

# -------------------------------------------------
# INTERFACE
# -------------------------------------------------

pergunta = st.text_area(
    "Digite sua pergunta jurídica ou cole seu caso:",
    height=200
)

btn = st.button("Gerar Parecer")

# -------------------------------------------------
# PROCESSAMENTO
# -------------------------------------------------

if btn and pergunta:

    with st.spinner("Analisando legislação e jurisprudência..."):

        contexto_lei = buscar_contexto(leis, pergunta)

        contexto_juris = buscar_jurisprudencia(juris, pergunta)

        prompt = f"""
        Você é um jurista especialista em direito brasileiro.

        Analise o caso abaixo.

        LEGISLAÇÃO RELEVANTE
        {contexto_lei}

        JURISPRUDÊNCIA
        {contexto_juris}

        CASO DO USUÁRIO
        {pergunta}

        Estruture a resposta com:

        1 - análise jurídica
        2 - enquadramento legal
        3 - jurisprudência aplicável
        4 - conclusão
        """

        resposta = model.generate_content(prompt)

        st.subheader("📄 Parecer Jurídico")

        st.write(resposta.text)

        st.download_button(
            "📥 Baixar parecer",
            resposta.text,
            file_name="parecer_juridico.txt"
        )

elif btn:
    st.warning("Digite uma pergunta ou caso jurídico.")

# -------------------------------------------------
# RODAPÉ
# -------------------------------------------------

st.markdown("---")
st.caption("DocSwift IA Jurídica • 2026")
