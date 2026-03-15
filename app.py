import streamlit as st
import google.generativeai as genai

# -------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -------------------------------

st.set_page_config(
    page_title="DocSwift IA Jurídica",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ DocSwift - Assistente Jurídico com IA")

st.write("Sistema de análise jurídica assistido por inteligência artificial.")

# -------------------------------
# CONFIGURAR API
# -------------------------------

api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ API KEY não encontrada. Configure no secrets.toml.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

# -------------------------------
# ENTRADA DO USUÁRIO
# -------------------------------

pergunta = st.text_area(
    "Digite sua pergunta jurídica ou descreva seu caso:",
    height=200
)

# -------------------------------
# BOTÃO
# -------------------------------

if st.button("Gerar parecer jurídico"):

    if not pergunta:
        st.warning("Digite uma pergunta ou caso.")
    else:

        with st.spinner("Analisando..."):

            prompt = f"""
            Você é um jurista especialista em direito brasileiro.

            Analise a situação abaixo.

            CASO:
            {pergunta}

            Estruture a resposta em:

            1 - análise jurídica
            2 - base legal aplicável
            3 - jurisprudência relevante
            4 - conclusão jurídica
            """

            resposta = model.generate_content(prompt)

            st.subheader("📄 Parecer Jurídico")

            st.write(resposta.text)

            st.download_button(
                "📥 Baixar parecer",
                resposta.text,
                file_name="parecer_juridico.txt"
            )

# -------------------------------
# RODAPÉ
# -------------------------------

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;color:gray">
⚖️ <b>DocSwift IA Jurídica</b> • 2026 <br>
Assistente jurídico baseado em inteligência artificial
</div>
""",
unsafe_allow_html=True
)
