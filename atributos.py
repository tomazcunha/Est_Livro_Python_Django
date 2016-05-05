# -*- encoding: utf-8 -*-

class Pessoa(object):
    atributo_de_classe = "Esse é um atributo de classe."

    def __init__(self):
        self.atributo_de_instancia = "Esse é um atributo de instância."

    def imprime_atributos(self):
        print "Imprimindo", Pessoa.atributo_de_classe
        print "Imprimindo", self.atributo_de_instancia

pessoa1 = Pessoa()
pessoa2 = Pessoa()

print Pessoa.atributo_de_classe     # já existe sem instancia

print pessoa1.atributo_de_classe    # o objeto também possui

print pessoa2.atributo_de_classe

Pessoa.atributo_de_classe = "Novo valor"

print Pessoa.atributo_de_classe

print pessoa1.atributo_de_classe

print pessoa1.atributo_de_instancia

pessoa1.atributo_de_instancia = "Novo valor de instância"

print pessoa1.atributo_de_instancia

pessoa1.atributo_de_classe = "valor de classe modificado por pessoa1"

print Pessoa.atributo_de_classe     # não mostra a alteraão de pessoa1

print pessoa1.atributo_de_classe    # só ela mesma mostra a alteração do atributo de classe

pessoa1.imprime_atributos()
