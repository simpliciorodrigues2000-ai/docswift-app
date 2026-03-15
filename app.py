import streamlit as st
import google.generativeai as genai

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="DocSwift IA Jurídica", page_icon="⚖️", layout="wide")

# CSS CLÁSSICO INSTITUCIONAL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lora:wght@400;600&display=swap');
    .stApp { background-color: #f4f1ea; color: #1a1a1a; font-family: 'Lora', serif; }
    h1, h2, h3 { font-family: 'Playfair Display', serif !important; color: #002d5e !important; border-bottom: 2px solid #daa520; padding-bottom: 10px; }
    [data-testid="stSidebar"] { background-color: #002d5e !important; color: white !important; }
    .stTextArea textarea { background-color: #ffffff !important; font-size: 1.1rem !important; border: 1px solid #c0c0c0 !important; border-radius: 4px; }
    .result-card { background-color: #ffffff !important; padding: 35px; border-left: 10px solid #002d5e; border-right: 1px solid #ddd; border-bottom: 1px solid #ddd; box-shadow: 5px 5px 15px rgba(0,0,0,0.05); color: #1a1a1a !important; line-height: 1.8; }
    .sidebar-img { border-radius: 8px; margin-bottom: 15px; border: 1px solid #daa520; }
    </style>
    """, unsafe_allow_html=True)

# 2. CONFIGURAR API
api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("⚠️ API KEY não encontrada.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash") # Flash para ser instantâneo

# 3. INTERFACE LATERAL
with st.sidebar:
    # Link da imagem da Deusa da Justiça
    st.markdown('<img src="https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=300&q=80" class="sidebar-img" width="100%">', unsafe_allow_html=True)
    st.title("DocSwift PRO")
    st.write("---")
    st.info("Algoritmo de análise processual e legislativa ativa.")
    st.write("📅 Base Legal: 2026")

# 4. INTERFACE PRINCIPAL
st.title("⚖️ DocSwift - Assistente Jurídico")

col1, col2 = st.columns([1, 1.3], gap="large")

with col1:
    st.subheader("📥 Objeto de Análise")
    pergunta = st.text_area(
        "Descreva o caso e cole as leis/artigos relevantes abaixo:",
        height=450,
        placeholder="Ex: Sou candidato da PMPR... Segundo o artigo X da lei Y..."
    )
    btn = st.button("Gerar Parecer Jurídico")

with col2:
    st.subheader("🔍 Parecer Técnico")
    if btn and pergunta:
        placeholder = st.empty()
        full_response = ""
        
        with st.spinner("⚖️ Analisando legislação e jurisprudência em tempo real..."):
            try:
                # O segredo está no prompt: ele força a IA a usar as leis que você colou
                prompt = f"""
                Você é um jurista especialista em direito brasileiro, mestre em redação de pareceres e recursos.
                
                Analise cuidadosamente o texto fornecido pelo usuário, que contém um CASO e possivelmente LEIS ou ARTIGOS.
                
                INSTRUÇÕES:
                1. Use preferencialmente as leis e artigos que o usuário colou no texto.
                2. Confrontre os fatos com a legislação (Planalto) e cite informativos do STF/STJ (Dizer o Direito).
                3. Se o caso for sobre concurso público, foque em princípios como razoabilidade e proporcionalidade.
                
                TEXTO DO USUÁRIO:
                {pergunta}
                
                ESTRUTURA DO PARECER:
                1 - ANÁLISE JURÍDICA DOS FATOS
                2 - ENQUADRAMENTO LEGAL (CITE OS ARTIGOS AQUI)
                3 - JURISPRUDÊNCIA APLICÁVEL
                4 - CONCLUSÃO E MINUTA DE RECURSO
                """
                
                # Streaming para velocidade máxima
                response = model.generate_content(prompt, stream=True)
                
                for chunk in response:
                    if chunk.text:
                        full_response += chunk.text
                        # O quadro agora tem escrita preta sobre fundo branco (estilo clássico)
                        placeholder.markdown(f'<div class="result-card">{full_response}▌</div>', unsafe_allow_html=True)
                
                placeholder.markdown(f'<div class="result-card">{full_response}</div>', unsafe_allow_html=True)
                
                st.download_button(
                    "📥 Baixar parecer oficial (.txt)",
                    full_response,
                    file_name="parecer_docswift.txt"
                )
            except Exception as e:
                st.error(f"Erro no processamento: {e}")
    else:
        st.markdown('<div style="color: #666; font-style: italic;">Aguardando entrada de dados para lavrar parecer.</div>', unsafe_allow_html=True)

# 5. RODAPÉ
st.markdown("---")
st.markdown(f"<center style='color: #888;'>DocSwift IA Jurídica | Desenvolvido por <b>Rodrigues do Nascimento Filho</b> • 2026</center>", unsafe_allow_html=True)
    
