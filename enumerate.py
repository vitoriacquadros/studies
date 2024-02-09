"""
enumerate -> enumera iteráveis e retorna um objeto enumerado
"""

lista = ['Batman', 'Robin', 'Wonder Woman']
lista.append('Coringa')

# lista_enumerada = enumerate(lista)
# print(next(lista_enumerada)) #next -> retorna o próximo valor de um iterador

# for i, nome in enumerate(lista):
#     print(i, nome)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla: ')
    for value in tupla_enumerada:
        print(f'\t{value}')