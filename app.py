import streamlit as st
import google.generativeai as genai

# 1. CONFIGURAÇÃO DE ALTA PERFORMANCE
st.set_page_config(page_title="DocSwift PRO - Inteligência Jurídica", page_icon="🛡️", layout="wide")

# CSS Avançado para Persuasão Visual
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Roboto', sans-serif; }
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stButton>button {
        background: linear-gradient(45deg, #b8860b, #daa520);
        color: white; border: none; font-weight: bold; height: 3.5em;
        transition: 0.3s; box-shadow: 0px 4px 15px rgba(218, 165, 32, 0.4);
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0px 6px 20px rgba(218, 165, 32, 0.6); }
    .status-box { padding: 20px; border-radius: 10px; background-color: #1e2130; border-left: 5px solid #daa520; }
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM A IA
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Chave de API ausente.")

model = genai.GenerativeModel('gemini-1.5-pro')

# 3. BARRA LATERAL ESTRATÉGICA
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3665/3665910.png", width=80)
    st.title("DocSwift PRO")
    st.markdown("---")
    nicho = st.selectbox("Selecione o Foco da Análise:", ["Concursos (PMPR/Polícia)", "Direito do Consumidor", "Contratos/Imobiliário"])
    st.warning("⚠️ **Atenção:** Prazos recursais são fatais.")
    st.divider()
    st.info("Algoritmo ajustado para Informativos do STF/STJ 2026.")

# 4. TELA PRINCIPAL
st.title("⚖️ DocSwift: Análise Legal Estratégica")
st.markdown(f"**Inteligência Ativa:** Especialista em {nicho}")

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown('<div class="status-box"><b>Passo 1:</b> Insira o relato do caso para encontrar ilegalidades.</div>', unsafe_allow_html=True)
    st.write("")
    relato = st.text_area("Descreva o problema aqui:", height=400, placeholder="Ex: Descreva aqui o motivo da inaptidão...")
    analisar = st.button("⚖️ EXECUTAR ANÁLISE DE IMPACTO")

with col2:
    if analisar and relato:
        with st.spinner("⚖️ Cruzando dados legais..."):
            try:
                prompt = f"Aja como um advogado consultor de elite em {nicho}. Analise o caso: {relato}"
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.download_button("📥 Baixar Recurso Estratégico", data=response.text, file_name="defesa_docswift.txt")
            except Exception as e:
                st.error(f"Erro: {e}")
    else:
        st.info("Aguardando inserção de dados para iniciar a perícia digital.")

# 5. RODAPÉ (NOME ALTERADO)
st.markdown("---")
st.markdown(f"<center><b>Consultoria Desenvolvida por Rodrigues do Nascimento Filho</b><br>DocSwift IA © 2026 - Tecnologia de Ponta para Defesa do Cidadão</center>", unsafe_allow_html=True)
