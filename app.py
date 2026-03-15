
import streamlit as st
import google.generativeai as genai

# 1. SETUP INSTITUCIONAL
st.set_page_config(page_title="DocSwift | Consultoria Jurídica", page_icon="⚖️", layout="wide")

# CSS CLÁSSICO: Mármore, Azul Marinho e Dourado Antigo
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');
    
    /* Fundo em tom Off-White / Mármore claro para suavidade */
    .stApp {
        background-color: #f4f1ea; 
        color: #1a1a1a;
        font-family: 'Lora', serif;
    }
    
    /* Títulos em estilo clássico (Playfair Display) */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #002d5e !important; /* Azul Marinho Acadêmico */
        border-bottom: 2px solid #daa520;
        padding-bottom: 10px;
    }

    /* Barra lateral em Azul Marinho */
    [data-testid="stSidebar"] {
        background-color: #002d5e !important;
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] * { color: white !important; }

    /* Caixas de texto simulando papel de pergaminho ou ofício */
    .stTextArea textarea {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
        border: 1px solid #c0c0c0 !important;
        border-radius: 4px !important;
        font-size: 1.1rem !important;
        box-shadow: inset 2px 2px 5px rgba(0,0,0,0.05);
    }

    /* Botão com estilo de selo oficial */
    .stButton>button {
        background-color: #002d5e !important;
        color: #ffffff !important;
        font-family: 'Playfair Display', serif;
        font-weight: bold;
        border-radius: 2px;
        border: 1px solid #daa520;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #daa520 !important;
        color: #002d5e !important;
    }

    /* QUADRO DE RESPOSTA: Estilo Parecer Técnico */
    .result-card {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
        padding: 40px;
        border-radius: 2px;
        border-left: 10px solid #002d5e;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
        line-height: 1.8;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM O MOTOR PRO
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Chave de API ausente nos segredos do sistema.")

model = genai.GenerativeModel('gemini-1.5-pro')

# 3. INTERFACE
with st.sidebar:
    st.markdown("### 🏛️ DOCSWIFT")
    st.markdown("---")
    nicho = st.selectbox("Especialidade Jurisprudencial:", ["Concursos Públicos", "Direito Administrativo"])
    st.write("")
    st.caption("Sistema de Apoio à Decisão Jurídica - Versão Institucional 2026")

st.title("⚖️ DocSwift: Consultoria e Análise")
st.write("Análise técnica baseada na legislação vigente e súmulas dos tribunais superiores.")

col1, col2 = st.columns([1, 1.3], gap="large")

with col1:
    st.subheader("📥 Objeto de Análise")
    relato = st.text_area("Exponha os fatos ou transcreva o documento:", height=450, placeholder="Digite aqui os detalhes do caso...")
    btn_analisar = st.button("GERAR PARECER TÉCNICO")

with col2:
    st.subheader("🔍 Parecer Processual")
    if btn_analisar and relato:
        placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Lavrando parecer..."):
            try:
                prompt = f"Aja como um jurista renomado. Elabore um parecer clássico e formal sobre: {relato}. Use linguagem jurídica culta."
                response = model.generate_content(prompt, stream=True)
                
                for chunk in response:
                    if chunk.text:
                        full_response += chunk.text
                        placeholder.markdown(f'<div class="result-card">{full_response}▌</div>', unsafe_allow_html=True)
                
                placeholder.markdown(f'<div class="result-card">{full_response}</div>', unsafe_allow_html=True)
                st.download_button("📥 BAIXAR DOCUMENTO OFICIAL", data=full_response, file_name="parecer_docswift.txt")
            except Exception as e:
                st.error(f"Falha na comunicação com o motor de busca: {e}")
    else:
        st.info("Aguardando petição ou documentos para análise de mérito.")

# 4. RODAPÉ SOLENE
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"<center style='color: #666; font-style: italic;'>Desenvolvido por <b>Rodrigues do Nascimento Filho</b> | DocSwift IA © 2026</center>", unsafe_allow_html=True)
