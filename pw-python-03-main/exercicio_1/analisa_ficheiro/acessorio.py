import os
import json
def pede_nome():
    ficheiroExiste = False
    nomeFicheiro = ""
    while not ficheiroExiste:
        ficheiroExiste = False
        nomeFicheiro = input("Introduza nome de ficheiro (txt): ")
        if os.path.exists(nomeFicheiro):
            ficheiroExiste = True
        if (len(nomeFicheiro) >=  4):
            if nomeFicheiro[-1] != 't' or nomeFicheiro[-2] != 'x' or nomeFicheiro[-3] != 't':
                ficheiroExiste = False
            if nomeFicheiro[-4] != '.' and os.path.exists(nomeFicheiro + ".txt"):
                ficheiroExiste = True
                nomeFicheiro = nomeFicheiro + ".txt"
    return nomeFicheiro

def gera_nome(nomeFicheiro):
    conteudoTxt = ""
    try:
        with open(nomeFicheiro, "r") as ficheiro:
            conteudoTxt = ficheiro.read()

        inicioExtensao = ""
        extJson = ""
        for carac in nomeFicheiro:
            if inicioExtensao != ".":
                extJson += carac
            if (carac == "."):
                inicioExtensao = "."

        nomeFicheiro = extJson + "json"

        with open(nomeFicheiro, "w") as ficheiro:
            json.dump(conteudoTxt, ficheiro)

    except OSError:
        print("Ficheiro nao existe")


