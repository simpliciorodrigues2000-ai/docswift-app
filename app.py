
import streamlit as st
import google.generativeai as genai

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="DocSwift IA", page_icon="⚖️", layout="wide")

# --- CONFIGURAÇÃO DE SEGURANÇA ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Erro: Chave de API não configurada nos Secrets do Streamlit.")

model = genai.GenerativeModel('gemini-1.5-pro')

# --- INTERFACE ---
with st.sidebar:
    st.title("🛡️ DocSwift")
    categoria = st.selectbox("Selecione o nicho:", ["Concursos Públicos", "Direito do Consumidor", "Imobiliário/Contratos", "Geral"])
    st.info("Conectado ao Planalto e Dizer o Direito.")

st.title("⚖️ DocSwift: Análise Legal Estratégica")
st.markdown(f"**Analisando em:** {categoria}")

texto_usuario = st.text_area("Descreva o caso ou cole o texto do documento:", height=250)

if st.button("Executar Análise"):
    if texto_usuario:
        with st.spinner("Analisando leis e jurisprudência..."):
            prompt = f"Analise como o DocSwift Engine (especialista em {categoria}) com foco no Planalto e Dizer o Direito: {texto_usuario}"
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Erro: {e}")
    else:
        st.warning("Por favor, digite algo para analisar.")
