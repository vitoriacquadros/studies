'''
Fatiamento de string 

012345678
Olá mundo 
-987654321
Fatiamento [i:f:p] [::]
obs.: a função len retorna quantidade de caracteres na string
'''

v = 'Olá mundo'

print(v[4])

print(len(v))

def inverte(frase): # função inverte frase
    return frase[::-1]

dado = input('Insira uma frase e veja ela ao contrário: ')
a = dado[::-1]

print(inverte(dado)) # usando função inverte dado 

