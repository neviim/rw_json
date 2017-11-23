# -*- coding: utf-8 -*-
# ler e grava um arquivo status com variaveis em json
# Neviim - 2017
# V-0.1.04
import json


# Classe para gravar e ler variaveis em um arquivo json.
class RWstatus_variaveis(object):
    """ docstring for RWstatus_variaveis.
            Uso:
                status = RWstatus_variaveis(<path>, <nome_arquivo>)
    """
    def __init__(self, path='../data'):
        ''' parametros:
                path = caminho do diretorio em de encontra o arquivo.
                nome = nome do arquivo a ser lido.

                - Caso não seja passado parametro assumira o default
                    path em: "../data"
                    arquivo: "data"

                - A extenção esta definida altomaticamente

                - É esperado que o arquivo jason esteja criado, ele pode conter\
                  qualquer conjunto de variaveis dentro do mesmo a jestão de\
                  como chamar a variavel e o nome dada a ela sera de\
                  responsabilidade do utilizador.
        '''
        super(RWstatus_variaveis, self).__init__()
        self.path = path
        self.extensao = '.json'

    def criar(self, arquivo, titulo):
        ''' criar um novo arquivo json pré-definido.
                Parametros:
                    arquivo = nome do arquivo json.
                    titulo  = titulo de identificação do dicionatio criado.
        '''
        data = {titulo: {'nome': 'jads', 'versão': 0.1}}
        with open(self.path +'/'+ arquivo + self.extensao, 'w') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)
        return True

    def ler(self, arquivo):
        ''' le os dados do arquivo json especificado.
                Uso:
                    rwStatus.ler()
        '''
        with open(self.path +'/'+ arquivo + self.extensao) as json_file:
            data = json.load(json_file)
        return data

    def grava(self, arquivo, data):
        ''' grava status de variaveis do sistema em um arquivo.
                - Parametros:
                    data = é um dicionario json, com a estrutura que deseja\
                           salvar em arquivo.

                - A formatação sera identada em tab 4.
                - A path e o nome do arquivo é assumido de path + nome.
        '''
        with open(self.path +'/'+ arquivo + self.extensao, 'w') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)
        return True

    def add_variavel(self, arquivo, titulo, variavel, valor):
        ''' adiciona uma nova variavel ao dicionario.
                Parametro:
                    arquivo   = nome do arquivo a ser criada a nova variavel
                    titulo    = titulo do grupo de variaveis
                    variavel  = nome da variavel a ser adicionada
                    valor     = conteudo desta variavel

                Uso:
                    rwStatus.add_variavel('arquivo', 'titulo', 'variavel', 'conteudo')

                Returna:
                    True  = se a variavel for cadastrada com sucesso.
                    False = esta variavel ja esta cadastrada neste dicionario.
        '''
        data = self.ler(arquivo)
        # verifica se a variavel ja esta cadastrada.
        if (variavel in data[titulo]):
            print('Esta variavel ja esta cadastrada, tente outro nome.')
            return False

        # atribui uma nova variavel ao dicionario.
        data[titulo][variavel] = valor
        self.grava(arquivo, data)
        return True

    def del_variavel(self, arquivo, titulo, variavel):
        ''' deleta uma variavel de um dicionario
                Parametros:
                    arquivo   = nome do arquivo a ser criada a nova variavel
                    titulo    = titulo do grupo de variaveis
                    variavel  = nome da variavel a ser adicionada

                Uso:
                    rwStatus.del_variavel(arquivo, 'clube', 'jads')

                Retorna:
                    True  = variavel deletada com sucesso.
                    False = variavel especificada não foi encontrada.
        '''
        data = self.ler(arquivo)
        # verifica se a variavel esta cadastrada.
        if (variavel in data[titulo]):
            # atribui uma nova variavel ao dicionario.
            data[titulo].pop(variavel)
            self.grava(arquivo, data)
            return True
        # retorna falso se a variavel não foi encontrada no dicionario.
        return False

    def set_valor(self, arquivo, titulo, variavel, valor):
        ''' seta um valor a uma variavel
                Parametros:
                    arquivo   = nome do arquivo a ser criada a nova variavel
                    titulo    = titulo do grupo de variaveis
                    variavel  = nome da variavel a ser adicionada
                    valor     = valor a ser adicionado a variavel

                Uso:
                    rwStatus.set_valor(arquivo, 'clube', 'neviim', 10)

                Retorna:
                    True  = variavel deletada com sucesso.
                    False = variavel especificada não foi encontrada.
        '''
        data = self.ler(arquivo)
        # verifica se a variavel esta cadastrada.
        if (variavel in data[titulo]):
            # verdadeiro, atribui um valor a ela.
            data[titulo][variavel] = valor
            self.grava(arquivo, data)
            return True
        # retorna false caso esta variavel não seja encontrada.
        return False

    def incrementa(self, arquivo, titulo, variavel, valor=1):
        ''' incremente 1 ao valor corrente da variavel dada.
                Parametros:
                    arquivo   = nome do arquivo a ser criada a nova variavel
                    titulo    = titulo do grupo de variaveis
                    variavel  = nome da variavel a ser adicionada
                    valor     = valor a ser incrementado, omitido ele valera 1.

                Uso:
                    rwStatus.incremento(arquivo, 'clube', 'neviim', 1)

                Retorna:
                    True  = valor incrementado com sucesso.
                    False = erro ao implementar o valor.
        '''
        data = self.ler(arquivo)
        # verifica se a variavel esta cadastrada.
        if (variavel in data[titulo]):
            # verdadeiro, atribui um valor a ela.
            data[titulo][variavel] = data[titulo][variavel] + valor
            self.grava(arquivo, data)
            return True
        # retorna false caso esta variavel não seja encontrada.
        return False

# teste de uso da classe RWstatus_variaveis
if __name__ == '__main__':
    rwStatus = RWstatus_variaveis('../data')
    arquivo  = 'rw_jads'

    # criando um arquivo novo
    #rwStatus.criar(arquivo, 'clube')

    # adiciona uma nova variavel a um dicionario
    rwStatus.add_variavel(arquivo, 'clube', 'jads', 1000)
    print(rwStatus.ler(arquivo))

    # altera um valor de uma variavel do dicionario
    rwStatus.set_valor(arquivo, 'clube', 'jads', 2000)
    print(rwStatus.ler(arquivo))

    # remove uma variavel do dicionario
    rwStatus.del_variavel(arquivo, 'clube', 'jads')
    print(rwStatus.ler(arquivo))

    # incrementa o valor passado a variavel especificada.
    rwStatus.incrementa(arquivo, 'clube', 'neviim', 1)
    print(rwStatus.ler(arquivo))
