# -*- coding: utf-8 -*-

# uni = u"olá"
# print uni

print type("ola")
print type("olá")
print type(u"olá")
print "Ola mundo"[4]
print "Ola mundo"[4:]
print "Ola munod"[2:5]
print "\tx"     # tabulação

a = "Olá"
print a

# b = a.decode("latin1")
# print b
#     print b
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 2-3: ordinal not in range(128)

# print b.encode("ascii")

# f = ru"C:\Diretório"      # diz sintaxe errada
f = r"C:\Diretório"
print f

# formatação com print
print "String %s" % ("formatada",)

print "Valor de spam: %(spam)d; " \
"valor de eggs: %(eggs)d" % ({'spam': 1, 'eggs': 2})

print "Cotação do dólar: %1.2f" % (2.1,)

print "Cotação do dólar: %1.2f" % (2.156,)

print "Desconto de %03d%%" % (35,)

print "|%d|%5d|%-5d|%05d|" % (3,3,3,3)

print "%g e %g" %(0.0005, 0.00005)

print "%015.5f" % (5.015,)

a = "spam"
print "%s" % a

x = "primeiro = {a} , segundo = {b} "
print x.format(a=1, b=2)

d = {'a': 10, 'b': 20}
z = "Alatura = {0[a]} , Largura = {0[b]}"
print z.format(d)
