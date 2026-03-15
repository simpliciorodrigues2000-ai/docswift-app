import streamlit as st
import google.generativeai as genai

# 1. SETUP DE ALTA PERFORMANCE & VISUAL PREMIUM
st.set_page_config(page_title="DocSwift PRO | Inteligência Estratégica", page_icon="⚖️", layout="wide")

# CSS PERSONALIZADO (DESIGN DE ELITE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top right, #0a192f, #000000);
        color: #e6f1ff;
        font-family: 'Inter', sans-serif;
    }
    
    /* Títulos em estilo futurista */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 2px;
        color: #daa520 !important;
        text-shadow: 0px 0px 10px rgba(218, 165, 32, 0.3);
    }

    /* Caixa de texto com efeito de vidro */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: #ffffff !important;
        border: 1px solid rgba(218, 165, 32, 0.3) !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px);
    }

    /* Botão IMPACTANTE */
    .stButton>button {
        background: linear-gradient(90deg, #b8860b 0%, #daa520 100%);
        color: #000 !important;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        border: none;
        border-radius: 30px;
        padding: 1rem 2rem;
        transition: all 0.4s ease;
        box-shadow: 0px 0px 20px rgba(218, 165, 32, 0.4);
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 35px rgba(218, 165, 32, 0.7);
        color: #fff !important;
    }

    /* Sidebar elegante */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.8);
        border-right: 1px solid #daa520;
    }

    /* Card de resposta */
    .result-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. INTELIGÊNCIA ARTIFICIAL
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Chave de API ausente.")

model = genai.GenerativeModel('gemini-1.5-flash')

# 3. CONTEÚDO LATERAL
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🛡️</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #daa520;'>DOCSWIFT PRO</h3>", unsafe_allow_html=True)
    st.write("")
    nicho = st.selectbox("Módulo Operacional:", ["Concursos Militares", "Direito Administrativo", "Geral"])
    st.divider()
    st.caption("Tecnologia de criptografia e análise rápida ativa.")

# 4. ÁREA DE COMANDO
st.title("⚖️ DOCSWIFT ENGINE")
st.markdown("<p style='color: #8892b0;'>Análise Estratégica de Alta Performance</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.write("### 📥 INPUT")
    relato = st.text_area("Insira os fatos para triagem:", height=300, placeholder="Ex: Relato de inaptidão em exame...")
    if st.button("ANALISAR AGORA"):
        st.session_state.analisar = True
    else:
        if 'analisar' not in st.session_state:
            st.session_state.analisar = False

with col2:
    st.write("### 🔍 OUTPUT")
    if st.session_state.analisar and relato:
        placeholder = st.empty()
        full_response = ""
        
        with st.spinner("⚡ PROCESSANDO..."):
            try:
                prompt = f"Aja como um jurista sênior. Analise com foco em {nicho}: {relato}"
                response = model.generate_content(prompt, stream=True)
                
                # Container estilizado para a resposta
                container = st.container()
                for chunk in response:
                    full_response += chunk.text
                    placeholder.markdown(f'<div class="result-card">{full_response}▌</div>', unsafe_allow_html=True)
                
                placeholder.markdown(f'<div class="result-card">{full_response}</div>', unsafe_allow_html=True)
                st.download_button("📥 EXPORTAR PARECER", data=full_response, file_name="docswift_analise.txt")
            except Exception as e:
                st.error(f"Erro no sistema: {e}")
    else:
        st.markdown('<div style="border: 1px dashed #444; padding: 50px; text-align: center; color: #444; border-radius: 20px;">Aguardando entrada de dados para iniciar varredura legal.</div>', unsafe_allow_html=True)

# 5. ASSINATURA (NOME REDUZIDO)
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"<center style='color: #444; border-top: 1px solid #222; padding-top: 20px;'>DESENVOLVIDO POR <b style='color: #666;'>RODRIGUES DO NASCIMENTO FILHO</b><br>DOCSWIFT IA © 2026</center>", unsafe_allow_html=True)
