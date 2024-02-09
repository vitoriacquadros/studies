"""
Introdução ao desempacotamento de listas e tuplas.

Desempacotamento em Python é a capacidade de atribuir múltiplos valores a múltiplas variáveis com uma única declaração.
Por exemplo, se você tem uma lista ou tupla com vários elementos, você pode atribuir cada elemento a uma variável diferente.
Utilizando métodos como o *args e **kwargs, você pode desempacotar listas e dicionários em argumentos de função.

"""

# _, _, nome2, *_  = ['Maria', 'Helena', 'Gustavo', 'Theodoro']
# print(nome2, _)


"""
Tuplas são imutáveis, mas você pode desempacotar uma tupla em variáveis individuais.

"""

nomes = ('Maria', 'Helena', 'Gustavo', 'Theodoro')
nome1, nome2, nome3, nome4 = nomes
print(nome1, nome2, nome3, nome4)
