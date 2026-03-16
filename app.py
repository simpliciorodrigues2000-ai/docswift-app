import streamlit as st
from openai import OpenAI

from busca_legislacao import buscar_legislacao
from busca_jurisprudencia import buscar_jurisprudencia
from gerador_pecas import gerar_peca

st.set_page_config(
    page_title="DocSwift IA Jurídica",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ DocSwift IA Jurídica")

# API
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("API KEY não encontrada.")
    st.stop()

pergunta = st.text_area(
    "Descreva seu caso jurídico:",
    height=200
)

tipo = st.selectbox(
    "Tipo de resposta",
    ["parecer", "denuncia", "habeas corpus"]
)

if st.button("Analisar"):

    if not pergunta:
        st.warning("Digite uma pergunta.")
        st.stop()

    # legislação
    st.subheader("📑 Legislação")

    legislacao = buscar_legislacao(pergunta)

    st.write(legislacao)

    # jurisprudência
    st.subheader("📚 Jurisprudência")

    jurisprudencia = buscar_jurisprudencia(pergunta)

    st.write(jurisprudencia)

    # peça jurídica
    if tipo != "parecer":

        st.subheader("📄 Peça Jurídica")

        peca = gerar_peca(tipo, pergunta)

        st.write(peca)

    # parecer IA
    else:

        try:

            prompt = f"""
            Analise juridicamente o seguinte caso.

            CASO:
            {pergunta}

            LEGISLAÇÃO:
            {legislacao}

            JURISPRUDÊNCIA:
            {jurisprudencia}

            Estruture em:

            1 análise jurídica
            2 base legal
            3 jurisprudência
            4 conclusão
            """

            resposta = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role":"system","content":"Você é um jurista especialista em direito brasileiro."},
                    {"role":"user","content":prompt}
                ]
            )

            st.subheader("⚖️ Parecer Jurídico")

            st.write(resposta.choices[0].message.content)

        except:

            st.error("Erro ao consultar IA.")
