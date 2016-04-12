# -*- coding: utf-8 -*-

# http://br.lipsum.com/feed/html
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed urna ligula, suscipit vel mauris ut, euismod pharetra eros. Nunc eu scelerisque elit. Donec eget commodo leo. Integer posuere egestas tristique."

lor = "Lorem ipsum dolor sit amet"

# -------------------------------------------------------------------------------------
# .capitalize()
"".capitalize()     # primeiro caractere em maiúsculo.

    # "exemplo".capitalize()
    print "exemplo".capitalize()
    print lorem.capitalize()


# -------------------------------------------------------------------------------------
# .center(largura)
"".center(largura)    # centraliza usando espaços em branco nos lados

    print lor.center(100) # largura de 100 caracteres


# -------------------------------------------------------------------------------------
# .count()
"".count()      # conta substrings

    num_lt = lorem.count("a")
    print "lorem 'a' = ", num_lt


    # -------------------------------------------------------------------------------------
    letras =("a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","v","x","z","w","y","k")
    letras_valor ={}

    for letra in letras:
        letras_valor[letra] = lorem.count(letra)
        # print letra , lorem_full.count(letra)

    print sorted(letras_valor.values())

    # -------------------------------------------------------------------------------------
    # http://defpython.blogspot.com.br/2007/01/conhecendo-os-dicionrios.html
    items = [('nome','igor'), ('idade', 18), ('curso','python')]
    d = dict(items)
    print d
    # {'idade': 18, 'curso': 'python', 'nome': 'igor'}


# -------------------------------------------------------------------------------------
# .endswith()
"".endswith()       # retorna true, caso a string termine com a substring

    etrue = lorem.endswith("tristique.")
    print etrue


# -------------------------------------------------------------------------------------
# .encode(), .decode()
"".encode()
"".decode()     # codifica/ decodifica string unicode em string (str), utilizando condificação especificada

    #
    ola = u"Olá"
    print ola

    ola_utf = ola.encode("utf-8")
    print "ola_utf: ", ola_utf

    ola_latin1 = ola.encode("latin1")
    print "ola_latin1: ", ola_latin1

    ola_utf_dec = ola_utf.decode("utf-8")
    print "ola_utf_dec: ", ola_utf_dec

    ola_latin1_dec = ola_latin1.decode("latin1")
    print "ola_latin1_dec: ", ola_latin1_dec


# -------------------------------------------------------------------------------------
# .expandtabs()
"".expandtabs()      # transforma tabulação em espaço

    >>> "\t".expandtabs() # padrão 8 espaços
    >>> "\t".expandtabs(4) # 4 espaços
    >>> len("\t".expandtabs())


# -------------------------------------------------------------------------------------
# .find()
"".find()

    # retorna a posição da primeira ocorrência de uma substring dentro da string a partir da
    # posição início até a posição fim.
    # se nada for encontrado, retorna -1.
    # finda não é muito recomendado, melhor usar o método .index() que retorna erro e não número
    # quando não encontra a substring.
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed urna ligula, suscipit vel mauris ut, euismod pharetra eros. Nunc eu scelerisque elit. Donec eget commodo leo. Integer posuere egestas tristique."

    "string".find("substring", posi_inic_busca, posi_final_busca)

    "abcde".find("c")
    "abcde".find("a")
    "abcde".find("z")
    "abcde".find("")
    lorem.find("adipiscing")
    lorem.find("do")
    lorem.find("do",1)

    lorem.find("elit", 1, 61)
    51

# -------------------------------------------------------------------------------------
# .format()
"".format()     # Substitui valores do template por parâmetros passados pelo format.

    "{1} {nome} {0}".format("parametro0", "parametro1", nome="Python")


# -------------------------------------------------------------------------------------
# .index()
"".index()      # o mesmo que .find() só que retorna exceção(valueErro) quando não encontra.

    "abcde".index("c")
    lorem.index("do")
    # 12
    lorem.index("do", 15)
    # 163

    # valueErro: substring not found


# -------------------------------------------------------------------------------------
# Retorna true caso a string seja composta.
"".isalpha()    # caracteres alfanumpericos
"".isdecimal()  # decimais      ((apenas para strings unicode))
"".isdigit()    # dígitos
"".islower()    # caracteres em letra minúscula (ignora caracteres acentuados)
"".isnumeric()  # numéricos     ((apenas para strings unicode))
"".isspace()    # espaços em branco
"".istitle()    # primeira letra de cada palavra em maiúcula
"".issupper()   #caracteres em maiúculo


# -------------------------------------------------------------------------------------
# 
