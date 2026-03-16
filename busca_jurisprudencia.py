import requests

def buscar_jurisprudencia(consulta):

    try:

        url = "https://jurisprudencia.stf.jus.br/api/search"

        params = {
            "q": consulta,
            "page": 1
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return "Não foi possível buscar jurisprudência."

        data = response.json()

        if "results" not in data:
            return "Nenhuma decisão encontrada."

        resultados = data["results"][:3]

        resposta = ""

        for r in resultados:

            resposta += f"""
            Tribunal: STF
            Processo: {r.get("processo","")}
            Relator: {r.get("relator","")}
            Ementa: {r.get("ementa","")}

            -----------------------
            """

        return resposta

    except Exception:

        return "Erro ao buscar jurisprudência."
