# -*- encoding: utf-8 -*-

class ClassePai1(object):
    def __init__(self):
        super(ClassePai1, self).__init__()
        print "Classe Pai 1"

class ClassePai2(object):
    def __init__(self):
        super(ClassePai2, self).__init__()
        print "Classe Pai 2"

class ClasseFilho(ClassePai1, ClassePai2):
    def __init__(self):
        super(ClasseFilho, self).__init__()
        print "Classe Filho"


pai1 = ClassePai1()

pai2 = ClassePai2()

filho = ClasseFilho()

print type(pai1)

print type(filho)

print isinstance(pai1, ClassePai1)

print isinstance(pai2, ClassePai2)

print isinstance(filho, ClasseFilho)
