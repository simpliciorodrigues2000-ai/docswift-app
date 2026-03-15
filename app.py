import streamlit as st
import google.generativeai as genai

# 1. SETUP DE ALTA VELOCIDADE
st.set_page_config(page_title="DocSwift PRO", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stButton>button {
        background: linear-gradient(45deg, #b8860b, #daa520);
        color: white; border: none; font-weight: bold; height: 3em;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO E CONFIGURAÇÃO DE VELOCIDADE
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Chave de API ausente.")

# Configurações para resposta rápida (baixa temperatura = menos hesitação)
generation_config = {
  "temperature": 0.3,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024, # Limita o tamanho para ser mais rápido
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

# 3. INTERFACE
with st.sidebar:
    st.title("DocSwift PRO")
    nicho = st.selectbox("Área:", ["Concursos (PMPR/Polícia)", "Geral"])
    st.info("🚀 MODO TURBO ATIVADO")

st.title("⚖️ DocSwift: Análise Estratégica")

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    relato = st.text_area("Descreva o caso:", height=300)
    analisar = st.button("⚖️ EXECUTAR AGORA")

with col2:
    if analisar and relato:
        placeholder = st.empty()
        full_response = ""
        
        try:
            # Otimização do Prompt para respostas mais curtas e diretas
            prompt = f"Seja direto e técnico. Analise como especialista em {nicho}: {relato}. Divida em: 1. Ilegalidade, 2. Artigo de Lei, 3. Sugestão Curta."
            
            response = model.generate_content(prompt, stream=True)
            
            for chunk in response:
                if chunk.text:
                    full_response += chunk.text
                    placeholder.markdown(full_response + "▌")
            
            placeholder.markdown(full_response)
            st.download_button("📥 Baixar", data=full_response, file_name="defesa.txt")
        except Exception as e:
            st.error(f"Erro: {e}")

# 4. RODAPÉ
st.markdown("---")
st.markdown(f"<center><b>Consultoria Desenvolvida por Rodrigues do Nascimento Filho</b><br>DocSwift IA © 2026</center>", unsafe_allow_html=True)
