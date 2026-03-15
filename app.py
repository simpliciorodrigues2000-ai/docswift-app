import streamlit as st
import google.generativeai as genai

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="DocSwift IA", page_icon="⚖️", layout="wide")

# --- CONFIGURAÇÃO DE SEGURANÇA (API KEY) ---
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Erro: Chave de API não configurada nos Secrets do Streamlit.")

model = genai.GenerativeModel('gemini-1.5-pro')

# --- ESTILIZAÇÃO CUSTOMIZADA ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #004a99;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (MENU LATERAL) ---
with st.sidebar:
    st.title("??? DocSwift")
    st.caption("Versão 1.0 - Compliance & Defesa")
    st.divider()
    
    categoria = st.selectbox(
        "Selecione o nicho de análise:",
        ["Concursos Públicos", "Direito do Consumidor", "Imobiliário/Contratos", "Defesa Administrativa Geral"]
    )
    
    st.divider()
    st.info("Sincronizado com: Portal do Planalto & Dizer o Direito (2026)")

# --- LÓGICA DE CONTEXTO POR CATEGORIA ---
instrucoes_nicho = {
    "Concursos Públicos": "Foque em editais, razoabilidade, proporcionalidade e informativos do Dizer o Direito sobre concursos (STJ/STF).",
    "Direito do Consumidor": "Foque no Código de Defesa do Consumidor (CDC), cláusulas abusivas e responsabilidade civil.",
    "Imobiliário/Contratos": "Foque na Lei do Inquilinato, Código Civil e equilíbrio nas relações contratuais.",
    "Defesa Administrativa Geral": "Foque no devido processo legal, contraditório, ampla defesa e legislação do Planalto."
}

# --- TELA PRINCIPAL ---
st.title("?? DocSwift: Análise Legal Estratégica")
st.write(f"**Categoria Ativa:** {categoria}")
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("?? Dados para Análise")
    texto_usuario = st.text_area(
        "Cole o trecho do documento ou descreva o problema abaixo:",
        placeholder="Ex: Fui reprovado no exame de visão da PMPR mesmo usando lentes...",
        height=300
    )
    
    arquivo = st.file_uploader("Ou envie o arquivo (PDF/Imagem)", type=['pdf', 'png', 'jpg'])

with col2:
    st.subheader("?? Veredito da Inteligência")
    
    if st.button("Executar Análise Profissional"):
        if texto_usuario or arquivo:
            with st.spinner("Consultando bases legais e jurisprudência..."):
                
                prompt_mestre = f"""
                CONTEXTO: {instrucoes_nicho[categoria]}
                TAREFA: Você é o DocSwift Engine. Analise o documento/relato abaixo confrontando-o com o Portal do Planalto e o site Dizer o Direito.
                
                DOCUMENTO DO USUÁRIO: {texto_usuario}
                
                ESTRUTURA DA RESPOSTA:
                1. RESUMO DOS FATOS: O que está acontecendo.
                2. ANÁLISE LEGAL (PLANALTO): Quais leis se aplicam.
                3. JURISPRUDÊNCIA (DIZER O DIREITO): Como os tribunais decidem casos assim.
                4. CONCLUSÃO E RISCOS: O documento é ilegal ou válido?
                5. MINUTA DE SOLUÇÃO: Escreva um rascunho de recurso ou resposta técnica.
                
                REGRAS: Seja formal. Não invente leis. Cite informativos reais se disponíveis.
                """
                
                try:
                    response = model.generate_content(prompt_mestre)
                    st.markdown(response.text)
                    
                    st.download_button(
                        label="?? Baixar Documento de Defesa",
                        data=response.text,
                        file_name=f"analise_docswift_{categoria.lower()}.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"Erro ao processar: {e}")
        else:
            st.warning("Por favor, forneça um texto ou arquivo para iniciar.")

st.markdown("---")
st.caption("Aviso: O DocSwift é uma ferramenta de suporte. Consulte sempre um advogado para decisões judiciais.")
