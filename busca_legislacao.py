import requests

def buscar_legislacao(tema):

    try:

        tema = tema.lower()

        leis = {

            "codigo penal": "https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm",
            "cp": "https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm",

            "codigo civil": "https://www.planalto.gov.br/ccivil_03/leis/2002/l10406.htm",
            "cc": "https://www.planalto.gov.br/ccivil_03/leis/2002/l10406.htm",

            "codigo de processo penal": "https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689.htm",
            "cpp": "https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689.htm",

            "codigo de processo civil": "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm",
            "cpc": "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm",

            "constituicao": "https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm",
            "cf": "https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm"

        }

        for chave in leis:

            if chave in tema:

                url = leis[chave]

                r = requests.get(url, timeout=10)

                if r.status_code == 200:

                    texto = r.text[:3000]

                    return f"Lei encontrada:\n{url}\n\nTrecho da legislação:\n{texto}"

        return "Legislação não identificada. Tente citar o código (CP, CPP, CC, CPC ou CF)."

    except Exception as e:

        return f"Erro ao buscar legislação: {str(e)}"
