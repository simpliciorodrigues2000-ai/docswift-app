import streamlit as st
import google.generativeai as genai

# 1. SETUP DE ALTA PERFORMANCE
st.set_page_config(page_title="DocSwift PRO | Elite Jurídica", page_icon="⚖️", layout="wide")

# Manter o visual premium que você aprovou
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    .stApp { background: radial-gradient(circle at top right, #0a192f, #000000); color: #e6f1ff; font-family: 'Inter', sans-serif; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #daa520 !important; text-shadow: 0px 0px 10px rgba(218, 165, 32, 0.3); }
    .stTextArea textarea { background-color: rgba(255, 255, 255, 0.05) !important; color: #ffffff !important; border: 1px solid rgba(218, 165, 32, 0.3) !important; border-radius: 15px !important; }
    .stButton>button { background: linear-gradient(90deg, #b8860b 0%, #daa520 100%); color: #000 !important; font-family: 'Orbitron', sans-serif; font-weight: bold; border-radius: 30px; box-shadow: 0px 0px 20px rgba(218, 165, 32, 0.4); }
    .result-card { background: rgba(255, 255, 255, 0.03); padding: 25px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

# 2. CONEXÃO COM O MODELO MAIS POTENTE (PRO)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Chave de API ausente.")

# Configuração para evitar travamentos em respostas longas
generation_config = {
  "temperature": 0.5, # Equilíbrio entre criatividade e precisão técnica
  "top_p": 0.95,
  "max_output_tokens": 2048, # Dobramos a capacidade de texto para análises profundas
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro", # A versão mais inteligente disponível
    generation_config=generation_config
)

# 3. INTERFACE DE COMANDO
with st.sidebar:
    st.markdown("<h3 style='color: #daa520;'>DOCSWIFT ENGINE</h3>", unsafe_allow_html=True)
    nicho = st.selectbox("Especialidade:", ["Concursos Públicos (PMPR/PC)", "Direito Administrativo", "Contratos"])
    st.divider()
    st.write("💎 **Modo:** Alta Precisão (Pro)")
    st.caption("Analise editais e documentos com o máximo de profundidade jurídica.")

st.title("⚖️ DOCSWIFT PRO: ELITE")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.write("### 📥 DADOS PARA PERÍCIA")
    relato = st.text_area("Insira o texto ou dúvida jurídica:", height=400, placeholder="Ex: Analise a legalidade da reprovação no exame odontológico do concurso PMPR...")
    btn_analisar = st.button("EXECUTAR ANÁLISE DE ALTA COMPLEXIDADE")

with col2:
    st.write("### 🔍 PARECER TÉCNICO")
    if btn_analisar and relato:
        placeholder = st.empty()
        full_response = ""
        
        with st.spinner("⏳ A IA está processando uma análise profunda... Isso pode levar alguns segundos."):
            try:
                # Prompt de alto nível para o modelo PRO
                prompt = f"""
                Aja como um jurista sênior e mestre em {nicho}. 
                Realize uma análise técnica, formal e extremamente fundamentada do seguinte caso:
                {relato}
                
                ESTRUTURA:
                1. EXAME DOS FATOS
                2. AMPARO LEGAL (Constituição, Leis Federais, Decretos)
                3. JURISPRUDÊNCIA (Informativos STF/STJ)
                4. CONCLUSÃO ESTRATÉGICA E RECOMENDAÇÃO
                """
                
                # Streaming para não travar a interface
                response = model.generate_content(prompt, stream=True)
                
                for chunk in response:
                    if chunk.text:
                        full_response += chunk.text
                        placeholder.markdown(f'<div class="result-card">{full_response}▌</div>', unsafe_allow_html=True)
                
                placeholder.markdown(f'<div class="result-card">{full_response}</div>', unsafe_allow_html=True)
                st.download_button("📥 EXPORTAR DOCUMENTO PRO", data=full_response, file_name="analise_pro_docswift.txt")
            
            except Exception as e:
                st.error(f"Ocorreu um erro no processamento. Tente novamente em instantes. Erro: {e}")
    else:
        st.markdown('<div style="border: 1px dashed #444; padding: 50px; text-align: center; color: #444; border-radius: 20px;">Sistema pronto para análise de alta complexidade.</div>', unsafe_allow_html=True)

# 4. RODAPÉ
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"<center style='color: #444; border-top: 1px solid #222; padding-top: 20px;'>DESENVOLVIDO POR <b style='color: #666;'>RODRIGUES DO NASCIMENTO FILHO</b><br>DOCSWIFT IA PRO © 2026</center>", unsafe_allow_html=True)
