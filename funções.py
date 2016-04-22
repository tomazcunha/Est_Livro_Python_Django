
# função simples com um parametro
def spam(parametro):
    print parametro

spam("eggs")


# parâmetro com valor padrão
def spam(x="eggs"):
    print x

spam()


# definindo uma variável
# passando ela como parametro
# retornando o resultado para ser impresso
x = 1
def spam(y):
    y = y + 1
    return y

print(spam(x))


# função que modifica uma lista
def spam(y):
    y[0] = "spam"

x = ["eggs", "eggs"]
spam(x)
print x


#
def spam(x, y="valor y", *outros, **outros_mais):
    print x, y, outros, outros_mais

spam(1)
spam(1, 2)
spam(1, 2, 3, 4, 5)
spam(1, 2, 3, 4, 5, proximo=6, mais_um=7)


#
def spam():
    return ("valor1", "valor2")
    print "Isto não será executado"

print spam()
print spam()[0]


# list comprehension
foo = {"ch1":1, "ch2":2, "ch3":3}
print ["O Valor de %s e %s" % (x, y) for x, y in foo.items()]

ham = "spam eggs and ham"
print "".join([char for char in ham if char != " ")
print "".join([char for char in ham if char != " " and char != "and"])
