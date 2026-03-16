import requests
from bs4 import BeautifulSoup

def buscar_legislacao(tema):

    url = f"https://www.planalto.gov.br/busca/?q={tema}"

    try:
        r = requests.get(url, timeout=5)

        soup = BeautifulSoup(r.text, "html.parser")

        resultados = []

        for link in soup.find_all("a", href=True)[:5]:
            texto = link.text.strip()
            href = link["href"]

            if texto:
                resultados.append(f"{texto} - {href}")

        return "\n".join(resultados)

    except:
        return "Não foi possível encontrar legislação."
