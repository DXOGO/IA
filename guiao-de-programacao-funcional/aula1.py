#Exercicio 1.1
# Dada uma lista, retorna o seu comprimento.
def comprimento(lista):
	if len(lista) == 0:
		return 0
	return 1+comprimento(lista[1:])

#Exercicio 1.2
# Dada uma lista de numeros, retorna a respectiva soma.
def soma(lista):
	if len(lista) == 0:
		return 0
	return lista[0] + soma(lista[1:])
	

#Exercicio 1.3
# Dada uma lista e um elemento, verifica se o elemento ocorre na lista. Retorna um valor booleano.
def existe(lista, elem):
	if not lista:
		return False
	
	if lista[0] == elem:
		return True

	return existe(lista[1:],elem)

#Exercicio 1.4
# Dadas duas listas, retorna a sua concatenaçao.
def concat(l1, l2):
	if l1 == []:
		return l2
	if l2 == []:
		return l1
	
	l1.append(l2[0])	# l1 + 1º elemento do l2 e volta a chamar a funçao
	return concat(l1,l2[1:])

#Exercicio 1.5
# Dada uma lista, retorna a sua inversa
def inverte(lista):
	if not lista:
		return []
	
	return inverte(lista[1:]) + [lista[0]]

#Exercicio 1.6
# Dada uma lista, verifica se forma uma capicua, ou seja, se, quer se leia da esquerda para a
# direita ou vice-versa, se obtem a mesma sequencia de elementos.
def capicua(lista):
	if not lista:
		return True
	
	if lista[0] == lista[-1]:
		return capicua(lista[1:-1])

	return False


#Exercicio 1.7
# Dada uma lista de listas, retorna a concatenaçao dessas listas.
def explode(lista):
	if not lista:
		return []

	return lista[0] + explode(lista[1:])

#Exercicio 1.8
# Dada uma lista, um elemento x e outro elemento y, retorna uma lista similar à lista de
# entrada, na qual x é substituido por y em todas as ocorrências de x.
def substitui(lista, x, y):	
	if not lista:
		return []
	
	previous=substitui(lista[1:], x, y)
	if lista[0] == x:			# se o 1º elemente é x ent retorna a mesma lista mas y em vez de x 
		return [y] + previous

	return [lista[0]] + previous		# caso contrario, retorna a mm lista	
	

#Exercicio 1.9
# Dadas duas listas ordenadas de números, calcular a união ordenada mantendo eventuais repetições 
def junta_ordenado(list1, list2):
	if list1 == []:
		return list2
	if list2 == []:
		return list1	# se A=0 ent A^B=B e vice-versa

	if list1[0] < list2[0]:
		l_temp= junta_ordenado(list1[1:], list2)
		return [list1[0]] + l_temp
		 
	l_temp2=junta_ordenado(list1, list2[1:]) 
	return [list2[0]] + l_temp2


#Exercicio 2.1
# Dada uma lista de pares, produzir um par com as listas dos primeiros e segundos elementos desses pares.
# separar([( a1, b1), ... (an, bn)]) = ([a1, ... an], [b1, ... bn])

# ([(1, 'a'), (2, 'b'), (3, 'c')]) == ([1,2,3], ['a','b','c'])

def separar(lista):
	if not lista:
		return [],[]

	list1, list2 = separar(lista[1:])
	
	return ( [lista[0][0]] + list1, [lista[0][1]] + list2 )

#Exercicio 2.2
# Dada uma lista l e um elemento x, retorna um par formado pela lista dos elementos de l
# diferentes de x e pelo numero de ocorrencias x em l

# separar([1, 6, 2, 5, 5, 2, 5, 2], 2) -> ([1 ,6 ,5 ,5 ,5 ], 3)

def remove_e_conta(lista, elem):
	if not lista:
		return [], 0

	listn, count = remove_e_conta(lista[1:], elem)
	if lista[0] == elem:
		return listn, count+1
	else:
		return [lista[0]] + listn, count

#Exercicio 3.1
# Dada uma lista, retornar o elemento que está à cabeça (ou seja, na posição 0)
def cabeca(lista):
	if not lista:
		return []

	return lista[0]

#Exercicio 3.2
# Dada uma lista, retornar a sua cauda (ou seja, todos os elementos à excepção do primeiro).
def cauda(lista):
	if not lista:
		return []

	return lista[1:]

#Exercicio 3.3
# Dado um par de listas com igual comprimento, produzir uma lista dos pares dos elementos homólogos.

# ([1,2,3], ['a','b','c']) == [(1, 'a'), (2, 'b'), (3, 'c')]

def juntar(l1, l2):
	if len(l1) != len(l2):
		return None

	if not l1: return []

	lista = juntar(l1[1:],l2[1:])

	return [(l1[0], l2[0])] + lista

#Exercicio 3.4
# Dada uma lista de números, retorna o menor elemento
# menor([1,2,3,0,5]) == 0
def menor(lista):
	
	pass
	#return min(lista)

#Exercicio 3.6
# Dada uma lista de números, calcular o máximo e o mı́nimo, retornando-os num tuplo
def max_min(lista):
	pass
