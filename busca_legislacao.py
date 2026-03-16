import requests

def buscar_legislacao(tema):

    url = f"https://www.planalto.gov.br/busca/?q={tema}"

    try:
        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            return r.text[:2000]

        return "Legislação não encontrada."

    except:
        return "Erro ao buscar legislação."
