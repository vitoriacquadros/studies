""" Using for loop 
    for -> é uma estrutura de repetição
    for -> para
    in -> em
    range -> sequência de números
    range(start, stop, step)
    start -> início
    stop -> parada
    step -> passo
    range(0, 10, 1) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    range(0, 10, 2) -> 0, 2, 4, 6, 8
    range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    range(0, 10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    range(0, 10, 3) -> 0, 3, 6, 9
"""
senha_salva = '123456'
senha_digitada = ''
repeticoes = 5

while senha_digitada != senha_salva:
    senha_digitada = input(f'Sua senha ({repeticoes}x) ')
        
    repeticoes += 1
        
print(repeticoes)
print('Aquele laço acima pode ter repetições infinitas')

"""
    Ex.: 2 
"""

texto = 'Python'

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
    print(novo_texto)
    

""" Iterável -> str, range, list, dict, tuple, set, frozenset, bytes, bytearray
    Iterador -> objeto que é capaz de iterar sobre um iterável
    Iteração -> processo de percorrer um iterável
    next -> função que retorna o próximo valor de um iterador
    iter -> função que retorna um iterador
    (__iter__) -> método mágico que retorna um iterador
    (__next__) -> método mágico que retorna o próximo valor de um iterador
    
"""
number = range(0,10,2) #start, stop, step
number2 = range(0, 100, 2) #todos numeros pares de 0 a 100 

for value in number:
    print(value)   
    
texto = 'Suellen'.__iter__() #isso printa o endereço de memória do iterador
texto = iter('Suellen') #isso printa o endereço de memória do iterador também!

iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
