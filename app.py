import streamlit as st

from busca_legislacao import buscar_legislacao
from busca_jurisprudencia import buscar_jurisprudencia
from analise_ia import gerar_parecer

st.set_page_config(
    page_title="DocSwift IA Jurídica",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ DocSwift IA Jurídica")

st.write("Assistente jurídico com inteligência artificial e fontes reais.")

# --------------------

tab1, tab2, tab3 = st.tabs([
    "⚖️ Parecer Jurídico",
    "📚 Jurisprudência",
    "📑 Legislação"
])

# --------------------
# PARECER
# --------------------

with tab1:

    caso = st.text_area("Descreva o caso jurídico:", height=200)

    if st.button("Gerar parecer jurídico"):

        with st.spinner("Buscando legislação..."):
            legislacao = buscar_legislacao(caso)

        with st.spinner("Buscando jurisprudência..."):
            jurisprudencia = buscar_jurisprudencia(caso)

        prompt = f"""
Você é um jurista especialista em direito brasileiro.

CASO:
{caso}

LEGISLAÇÃO:
{legislacao}

JURISPRUDÊNCIA:
{jurisprudencia}

Produza um parecer com:

1. síntese dos fatos
2. enquadramento jurídico
3. dispositivos legais
4. jurisprudência relevante
5. conclusão jurídica
"""

        with st.spinner("Gerando parecer..."):
            resposta = gerar_parecer(prompt)

        st.subheader("📄 Parecer Jurídico")

        st.write(resposta)

# --------------------
# JURISPRUDÊNCIA
# --------------------

with tab2:

    tema = st.text_input("Tema jurídico")

    if st.button("Buscar jurisprudência"):

        resultado = buscar_jurisprudencia(tema)

        st.write(resultado)

# --------------------
# LEGISLAÇÃO
# --------------------

with tab3:

    tema = st.text_input("Pesquisar legislação")

    if st.button("Buscar legislação"):

        resultado = buscar_legislacao(tema)

        st.write(resultado)
