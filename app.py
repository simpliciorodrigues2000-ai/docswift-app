import streamlit as st
import google.generativeai as genai

st.title("⚖️ DocSwift IA Jurídica")

# pegar API do secrets
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("API KEY não encontrada. Configure no secrets.toml")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

pergunta = st.text_area("Digite sua pergunta jurídica")

if st.button("Gerar análise"):

    prompt = f"""
    Você é um jurista especialista em direito brasileiro.

    Analise a seguinte situação:

    {pergunta}

    Estruture a resposta em:

    1. análise jurídica
    2. base legal
    3. jurisprudência
    4. conclusão
    """

    resposta = model.generate_content(prompt)

    st.subheader("Resultado")

    st.write(resposta.text)
    
