import requests

def buscar_jurisprudencia(tema):

    try:

        url = f"https://jurisprudencia.stj.jus.br/api/search?q={tema}"

        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            return r.text[:2000]

        return "Nenhuma jurisprudência encontrada."

    except:
        return "Erro ao buscar jurisprudência."
