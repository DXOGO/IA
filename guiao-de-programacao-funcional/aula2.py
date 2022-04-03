import math

#Exercicio 4.1
# (Implementar na forma de uma expressao-lambda:) Dado um numero inteiro, 
# retorna True caso o numero seja ımpar, e False caso contrario.
# lambda arguments : expression
impar = lambda x: False if x%2==0 else True

#Exercicio 4.2
# Dado um numero, retorna True caso o numero seja positivo, e False caso contrario
positivo = lambda x: True if x>0 else False

#Exercicio 4.3
# Dados dois numeros, x e y, retorna True caso |x| < |y|, e False caso contrario.
comparar_modulo = lambda x, y: True if abs(x) < abs(y) else False 

#Exercicio 4.4
# Dado um par (x, y), representando coordenadas cartesianas de um ponto no plano XY,
# retorna um par (r, θ), correspondente às coordenadas polares do mesmo ponto
cart2pol = lambda x,y: (math.sqrt(x*x+y*y), math.atan2(y,x))    # formula da net 

#Exercicio 4.5
# Dadas 3 funçoes de duas entradas, f, g e h, retorna uma funçao de 3 entradas, x, y e z, 
# cujo resultado é dado por: h( f(x, y), g(y, z) )
f = lambda x, y: x + y
g = lambda x, y: x * y
h = lambda x, y: x < y

ex5 = lambda f,g,h: (lambda x,y,z: h( f(x,y), g(y,z) ))  

#Exercicio 4.6
def quantificador_universal(lista, f):
    pass

#Exercicio 4.9
def ordem(lista, f):
    pass

#Exercicio 4.10
def filtrar_ordem(lista, f):
    pass

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    pass
