# conjunto = {1, 2, 3, 4} # pré definido em ordem crescente;
# conjunto.add(5)
# conjunto.discard(2)
# print (conjunto)

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4}
conjunto_uniao = conjunto1.union (conjunto2) #Unir conjuntos
print ('União dos conjuntos: {}' .format(conjunto_uniao)) 
conjunto_interseccao = conjunto1.intersection (conjunto2) # encontrar os n° iguais nos conjuntos
print ('Número de Interseção entre os conjuntos: {}' .format(conjunto_interseccao))
conjunto_diferenca1 = conjunto1.difference (conjunto2) # diferença dos numeros de conj 1 para 2
print ('Diferença conjunto 1 para o 2: {}' .format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference (conjunto1) # diferença dos numeros de conj 2 para 1
print ('Diferença conjunto 2 para o 1: {}' .format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2) # Contrario da Intersection
print ('Diferença Simetrica: {}' .format(conjunto_diff_simetrica))

conjunto_subset = conjunto_a.issubset (conjunto_b)
print ("{} o conjunto A é um sub conjunto do B pois contém os mesmo numeros." .format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset (conjunto_a)
print ("{} o conjunto B é um super conjunto do A pois contém todos os elementos de A." .format(conjunto_superset))

lista = ['cão', 'gato', 'elefante', 'gato', 'cão']
print (lista)
conjunto_animais = set(lista) # retirar duplicidade transformando de lista para conjunto (set)
print (conjunto_animais)
lista_animais = list(conjunto_animais) #reconverter em lista
print (lista_animais)

def soma(a, b):
    return a + b

print(soma(1, 2))
