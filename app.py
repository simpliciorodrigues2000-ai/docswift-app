import streamlit as st
import google.generativeai as genai

# 1. CONFIGURAÇÃO DE ALTA PERFORMANCE
st.set_page_config(page_title="DocSwift PRO", page_icon="🛡️", layout="wide")

# CSS para manter o visual VIP
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stButton>button {
        background: linear-gradient(45deg, #b8860b, #daa520);
        color: white; border: none; font-weight: bold; height: 3.5em;
        border-radius: 8px;
    }
    .status-box { padding: 15px; border-radius: 10px; background-color: #1e2130; border-left: 5px solid #daa520; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM A IA (FLASH MODE)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Chave de API ausente.")

# Trocado para o modelo FLASH para maior velocidade
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. BARRA LATERAL
with st.sidebar:
    st.title("DocSwift PRO")
    nicho = st.selectbox("Área:", ["Concursos (PMPR/Polícia)", "Direito do Consumidor", "Geral"])
    st.divider()
    st.info("Modo Turbo Ativado: Respostas em tempo real.")

# 4. TELA PRINCIPAL
st.title("⚖️ DocSwift: Análise Estratégica")

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown('<div class="status-box"><b>Entrada de Dados:</b></div>', unsafe_allow_html=True)
    relato = st.text_area("Descreva o caso:", height=300, placeholder="Ex: Fui considerado inapto...")
    analisar = st.button("⚖️ EXECUTAR ANÁLISE RÁPIDA")

with col2:
    if analisar and relato:
        # Espaço reservado para a resposta em tempo real
        placeholder = st.empty()
        full_response = ""
        
        with st.spinner("⚡ Processando instantaneamente..."):
            try:
                prompt = f"Como consultor em {nicho}, analise rapidamente: {relato}. Estruture em: Fatos, Base Legal e Minuta de Recurso."
                
                # MODO STREAMING: A IA escreve enquanto pensa
                response = model.generate_content(prompt, stream=True)
                
                for chunk in response:
                    full_response += chunk.text
                    placeholder.markdown(full_response + "▌")
                
                placeholder.markdown(full_response) # Finaliza sem o cursor
                
                st.download_button("📥 Baixar Defesa", data=full_response, file_name="defesa_docswift.txt")
            except Exception as e:
                st.error(f"Erro: {e}")
    else:
        st.info("Aguardando dados.")

# 5. RODAPÉ (NOME REDUZIDO)
st.markdown("---")
st.markdown(f"<center><b>Consultoria Desenvolvida por Rodrigues do Nascimento Filho</b><br>DocSwift IA © 2026</center>", unsafe_allow_html=True)
