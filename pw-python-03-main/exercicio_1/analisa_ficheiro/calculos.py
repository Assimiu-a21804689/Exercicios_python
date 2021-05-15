def calcula_linhas(nomeFicheiro):
    numeroLinhas = 1

    try:
        with open(nomeFicheiro, "r") as ficheiro:
            conteudoFicheiro = ficheiro.read()
            if (len(conteudoFicheiro) == 0):
                numeroLinhas = 0
            for caracter in conteudoFicheiro:
                if caracter == "\n":
                    numeroLinhas = numeroLinhas + 1
    except OSError:
        return 0


    return numeroLinhas

def calcula_carateres(nomeFicheiro):
    try:
        with open(nomeFicheiro, "r") as ficheiro:
            conteudoFicheiro = ficheiro.read()
            return len(conteudoFicheiro)

    except OSError:
        return 0

def calcula_palavra_comprida(nomeFicheiro):
    palavra = ""
    carPalavra = ""
    try:
        with open(nomeFicheiro, "r") as ficheiro:
            conteudoFicheiro = ficheiro.read()
            for caracter in conteudoFicheiro:
                if (caracter == " " or caracter == "\n"):
                    if len(carPalavra) > len(palavra):
                        palavra = carPalavra
                        carPalavra = ""
                else:
                    carPalavra = carPalavra + caracter

            if (len(carPalavra) > len(palavra)):
                palavra = carPalavra
            return palavra
    except OSError:
        return palavra

def calcula_ocorrencia_de_letras(nomeFicheiro):
    lista_ocorrencias = {}
    try:
        with open(nomeFicheiro, "r") as ficheiro:
            conteudoFicheiro = ficheiro.read()

            for caracter in conteudoFicheiro:
                if (lista_ocorrencias.get(caracter) == None):
                    lista_ocorrencias[caracter] = 1;
                else:
                    lista_ocorrencias[caracter] = lista_ocorrencias.get(caracter) + 1
            return lista_ocorrencias
    except OSError:
        return lista_ocorrencias