import streamlit as st
import requests
import time

# -----------------------------
# CONFIGURAÇÃO
# -----------------------------

st.set_page_config(
    page_title="DocSwift IA Jurídica",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ DocSwift IA Jurídica")

st.write("Assistente jurídico com busca real de legislação e jurisprudência.")

HF_API_KEY = st.secrets["HF_API_KEY"]

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

# -----------------------------
# CACHE PARA VELOCIDADE
# -----------------------------

@st.cache_data(ttl=3600)
def buscar_legislacao(tema):

    url = f"https://www.planalto.gov.br/busca/?q={tema}"

    try:
        r = requests.get(url, timeout=5)
        return r.text[:2000]
    except:
        return "Legislação não encontrada."


@st.cache_data(ttl=3600)
def buscar_jurisprudencia(tema):

    try:
        url = f"https://jurisprudencia.stj.jus.br/api/search?q={tema}"
        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            return r.text[:2000]

        return "Jurisprudência não encontrada."

    except:
        return "Erro na busca de jurisprudência."


@st.cache_data(ttl=3600)
def gerar_parecer(prompt):

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 700,
            "temperature": 0.2
        }
    }

    response = requests.post(MODEL_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return "Erro na geração de parecer."

    data = response.json()

    try:
        return data[0]["generated_text"]
    except:
        return str(data)

# -----------------------------
# INTERFACE
# -----------------------------

tab1, tab2, tab3 = st.tabs([
    "⚖️ Parecer Jurídico",
    "📚 Jurisprudência",
    "📑 Legislação"
])

# -----------------------------
# PARECER
# -----------------------------

with tab1:

    pergunta = st.text_area("Descreva o caso jurídico:", height=200)

    if st.button("Gerar parecer"):

        with st.spinner("Buscando legislação..."):

            legislacao = buscar_legislacao(pergunta)

        with st.spinner("Buscando jurisprudência..."):

            jurisprudencia = buscar_jurisprudencia(pergunta)

        prompt = f"""

Você é um jurista especialista em direito brasileiro.

Utilize APENAS as fontes fornecidas.

CASO:
{pergunta}

LEGISLAÇÃO:
{legislacao}

JURISPRUDÊNCIA:
{jurisprudencia}

Estruture o parecer em:

1. síntese dos fatos
2. enquadramento jurídico
3. dispositivos legais aplicáveis
4. jurisprudência relevante
5. conclusão jurídica
"""

        with st.spinner("Gerando parecer..."):

            resposta = gerar_parecer(prompt)

        st.subheader("📄 Parecer Jurídico")

        st.write(resposta)

# -----------------------------
# JURISPRUDÊNCIA
# -----------------------------

with tab2:

    tema = st.text_input("Tema jurídico")

    if st.button("Buscar jurisprudência"):

        resultado = buscar_jurisprudencia(tema)

        st.write(resultado)

# -----------------------------
# LEGISLAÇÃO
# -----------------------------

with tab3:

    tema = st.text_input("Pesquisar legislação")

    if st.button("Buscar legislação"):

        resultado = buscar_legislacao(tema)

        st.write(resultado)

# -----------------------------
# RODAPÉ
# -----------------------------

st.markdown("---")

st.markdown(
"""
⚖️ DocSwift IA Jurídica • 2026  
Assistente jurídico baseado em IA
"""
)
