import requests
import streamlit as st

HF_API_KEY = st.secrets["HF_API_KEY"]

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

def gerar_parecer(prompt):

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 700,
            "temperature": 0.2
        }
    }

    response = requests.post(MODEL_URL, headers=headers, json=payload)

    data = response.json()

    try:
        return data[0]["generated_text"]
    except:
        return str(data)
