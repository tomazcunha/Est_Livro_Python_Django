# -*- encoding: utf-8 -*-
# grep2.py - Segunda versão do nosso utilitário de busca

# Importar os Módulos os e sys para obter informação sobre o ambiente em que o programa está rodando.
import os
import sys

# criamos dois tipos de exceção que usaremos no nosso código.
class ParametroInvalido(Exception):
    pass

class ArquivoInvalido(Exception):
    pass

# Organizamos o nosso código em funções.
# Esta função busca uma string dentro de um arquivo.
def buscar_arquivo(str_busca, nome_arquivo):
    encontrado = False
    try:
        #abrimos o arquivo e o percorremos linha a linha
        arquivo = open(nome_arquivo)
        for numero_linha, linha in enumerate(arquivo):
            if str_busca not in linha:
                continue

            dados = (nome_arquivo, numero_linha + 1, linha.strip(os.linesep))
            print "%s:%s: %s" % dados
            encontrado = True
            arquivo.close()

    # se algo acontecer de errado ao abrir e ler o arquivo, geramos uma exceção do tipo ArquivoInvalido.
    except IOError:
        raise ArquivoInvalido("Acesso ao arquivo %s" % (nome_arquivo,))

    # se tudo deu certo retornamos um booleano indicando se encontramos a string dentro do arquivo.
    return encontrado

# percorrer uma linha com o nomes de arquivos procurando por uma string dentro deles (chamamos a função buscar_arquivo para isso)
def busca(str_busca, arquivos):
    encontrado = False
    for nome_arquivo in arquivos:
        if buscar_arquivo(str_busca, nome_arquivo):
            encontrado = True

    return encontrado

# Processar os parametros passados para nosso programa
def processa_parametros(parametros):
    try:
        str_busca = parametros[0]
        lista_arquivos = parametros[1:]

    # se não foi informado o número correto de parametros geramos uma exceção do tipo ParametroInvalido
    except IndexError:
        raise ParametroInvalido(u"Parâmetro(s) inválidos(s)")

    # A mesma exceção será gerada se nenhum arquivo for informado
    if not lista_arquivos:
        raise ParametroInvalido(u"Informe o(s) arquivos(s) onde realizar a busca")

    return str_busca, lista_arquivos

# bloco principal da nossa aplicação
if __name__ = "__main__":
    # Chamamos a função de processamento de parâmetros, e de busca da string nos arquivos
    # se algo acontecer de errado tratamos as exceções de maneira adequada informando ao usuário sobre os erros.
    try:
        str_busca, lista_arquivos = processa_parametros(sys.argv[1:])
        encontrado = busca(str_busca, lista_arquivos)
        sys.exit(int(not encontrado))   # errolevel 0 == True

    except ParametroInvalido, ex:
        print "Uso: %s str lista_arquivos"
        print >>sys.stderr, "ERRO:", unicode(ex)
        sys.exit(-1)

    except ArquivoInvalido, ex:
        print >>sys.stderr, "ERRO:", unicode(ex)
        sys.exit(-1)
