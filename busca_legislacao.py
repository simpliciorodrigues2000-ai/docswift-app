import requests
from bs4 import BeautifulSoup

def buscar_legislacao(termo):

    try:

        url = f"https://www.planalto.gov.br/busca/?q={termo}"

        r = requests.get(url, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        links = soup.find_all("a")

        resultados = []

        for l in links[:10]:

            texto = l.get_text().strip()

            if texto:
                resultados.append(texto)

        return "\n".join(resultados)

    except:

        return "Não foi possível buscar legislação."
