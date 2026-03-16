import PyPDF2

def ler_pdf(arquivo):

    texto = ""

    reader = PyPDF2.PdfReader(arquivo)

    for pagina in reader.pages:

        texto += pagina.extract_text()

    return texto
