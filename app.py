import streamlit as st
import google.generativeai as genai

from busca_legislacao import buscar_legislacao
from busca_jurisprudencia import buscar_jurisprudencia
from leitor_pdf import ler_pdf

st.set_page_config(
    page_title="DocSwift IA Jurídica",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ DocSwift IA Jurídica")

st.write("Assistente jurídico inteligente.")

# API
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    st.error("Configure sua API KEY no Secrets.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

# INPUT CASO
caso = st.text_area(
    "Descreva o caso jurídico:",
    height=200
)

# UPLOAD PDF
pdf = st.file_uploader(
    "Enviar edital ou documento (PDF)",
    type=["pdf"]
)

texto_pdf = ""

if pdf:

    texto_pdf = ler_pdf(pdf)

    st.success("PDF carregado.")

# BOTÃO
if st.button("Analisar caso"):

    if not caso:

        st.warning("Digite o caso.")

    else:

        with st.spinner("Buscando legislação..."):

            legislacao = buscar_legislacao(caso)

        with st.spinner("Buscando jurisprudência..."):

            jurisprudencia = buscar_jurisprudencia(caso)

        with st.spinner("Gerando parecer..."):

            prompt = f"""
Você é um jurista especialista em direito brasileiro.

CASO:
{caso}

DOCUMENTO ANALISADO:
{texto_pdf}

LEGISLAÇÃO:
{legislacao}

JURISPRUDÊNCIA:
{jurisprudencia}

Elabore um parecer jurídico completo contendo:

1. análise dos fatos
2. enquadramento legal
3. jurisprudência relevante
4. possibilidade de recurso
5. conclusão jurídica
"""

            resposta = model.generate_content(prompt)

        st.subheader("Parecer Jurídico")

        st.write(resposta.text)

        st.download_button(
            "Baixar parecer",
            resposta.text,
            file_name="parecer_docswift.txt"
        )
