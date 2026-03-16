def gerar_peca(tipo, caso):

    if tipo == "denuncia":

        return f"""
EXCELENTÍSSIMO SENHOR DOUTOR JUIZ DE DIREITO

O MINISTÉRIO PÚBLICO, no uso de suas atribuições constitucionais, vem oferecer

DENÚNCIA

em face do acusado, pelos fatos a seguir descritos:

FATOS

{caso}

TIPIFICAÇÃO

Os fatos narrados configuram, em tese, crime previsto na legislação penal brasileira.

Diante do exposto, requer o recebimento da presente denúncia e a citação do acusado.

Termos em que,
Pede deferimento.
"""

    if tipo == "habeas corpus":

        return f"""
EXCELENTÍSSIMO SENHOR DESEMBARGADOR PRESIDENTE DO TRIBUNAL

HABEAS CORPUS

Paciente: investigado
Autoridade coatora: autoridade policial

DOS FATOS

{caso}

DO DIREITO

A prisão ou constrangimento ilegal viola garantias constitucionais.

DO PEDIDO

Requer a concessão da ordem de habeas corpus.

Termos em que,
Pede deferimento.
"""

    return "Tipo de peça não identificado."
