# -*- coding: utf-8 -*-
# ler e grava um arquivo status com variaveis em json
# Neviim - 2017
# V-0.0.01
import json

# grava um arquivo json
def grava(data):
    with open('../data/data.json', 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
    return True

# ler um arquivo json
def ler():
    with open('../data/data.json') as json_file:
        data = json.load(json_file)
    return data

# testando o codigo
if __name__ == '__main__':

    # le o arquivo
    data = ler()
    print(data['status']['linha'])

    ''' Inicio, Aqui coloca o seu codigo... '''
    # soma um a variavel linha
    data['status']['linha'] = data['status']['linha']+1
    print(data['status']['linha'])
    ''' Fim, ao finalizar o codigo salva o arquivo json '''

    # grava o arquivo json
    grava(data)
