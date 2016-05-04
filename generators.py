# -*- encoding: utf-8 -*-
# generator.py - Exemplo de uso de generators

db = (
((2009, 01, 05), "rec1"),
((2009, 02, 05), "rec2"),
((2009, 03, 05), "rec3"),
((2009, 04, 05), "rec4"),
((2009, 05, 05), "rec5"),
((2009, 06, 06), "rec6"),
)

def busca(dt_ini, dt_fim):
    for rec in db:
        if rec[0] >= dt_ini and rec[0] <= dt_fim:
            msg = yield rec[1]
            if msg:
                print rec[1], msg

for row in busca((2009, 03, 01), (2009, 05, 01)):
    print row

b = busca((2009, 03, 01), (2009, 05, 01))
print b.next()
b.send("ok")
try:
    print b.next()
except StopIteration:
    pass



# ------------------------------------------------------------
# http://pythonclub.com.br/python-generators.html

def generator():
    n = 1
    print("Essa é uma função generator")
    yield n
    n += 1
    yield n
    n += 1
    yield n

a = generator()     # retorna um objeto mas não executa a função imediatamente

print a
<generator object generator at 0x7f458bb3c9b0>

next(a)

# ------------------------------------------------------------
# https://diofeher.wordpress.com/2011/04/12/explicando-iterables-generators-yield-no-python/

generator = (letra for letra in "hjasdfjhhjasdfg")
generator.next()
>>> "h"
generator.next()
>>> "j"

# ------------------------------------------------------------
#
def gerador():
    for i in range(10):
        yield i * 2

gera = gerador()
print gera
gera.next()

for gerado in gera:
    print gerado

>>> print gerador()
<generator object gerador at 0x7f458bb3cbe0>
>>> print gerador().next()
0
