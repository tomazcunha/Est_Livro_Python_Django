#-*- coding: utf-8 -*-
# MOstrando números pares com list conprehension

numeros = range(10)
pares = [ numero for numero in numeros if not numero % 2]

print "Pares: ", pares

# --------------------------
spam =[1,2,3,4]
eggs =["desenvolver", "em", "python"]
ham ="spam ovos e presunto"
foo ={"chave1": 1, "chave2": 2, "chave3": 3}
print "pow a**2: ", [pow(x, 2) for x in spam]
# operator.pow(a, b) ou operator.__pow__(a, b)
# Return a ** b, for a and b numbers.

print "pow a**2: se a>2 :", [pow(x, 2) for x in spam if x > 2]
print "eggs upper", [x.upper() for x in eggs]
print ["O Valor de %s e %s" % (x, y) for x, y in foo.items()]
print "".join([ char for char in ham if char != " " ])

func = 'struct_em_c_que_vai_virar_classe_em_pyhton'
print "".join([ x.capitalize() for x in func.split("_")])
