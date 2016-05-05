# -*- encoding: utf-8 -*-

class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome

class PessoaJuridica(Pessoa):
    def __init__(self, nome):
        super(PessoaJuridica, self).__init__(nome)
        self.cnpj = ""

class PessoaFisica(Pessoa):
    def __init__(self, nome):
        super(PessoaFisica, self).__init__(nome)
        self.cpf = ""

pessoa1 = Pessoa("tom")
pessoa2 = PessoaJuridica("tom")
pessoa3 = PessoaFisica("tom")

print issubclass(PessoaJuridica, Pessoa)

print issubclass(PessoaFisica, Pessoa)

print isinstance(pessoa1, Pessoa)

print isinstance(pessoa2, PessoaFisica)

print isinstance(pessoa3, PessoaFisica)
