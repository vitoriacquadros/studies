""" 
Exercício 4:
    
Faça um programa que peça ao usuário para digitar seu nome e sua idade
Se o nome e idade forem válidos, o programa deve imprimir uma mensagem
    Exiba: 
        "Olá, <nome>! Você tem <idade> anos."
        Seu nome invertido e sua idade ao contrário.
        Seu nome contém espaços? True ou False
        Seu nome tem {n} letras.
        Seu nome tem {n} vogais.
        Seu nome tem {n} consoantes.
        Seu nome tem {n} espaços.
        Seu nome tem {n} dígitos.
        A primeira letra do seu nome é <letra>
        A última letra do seu nome é <letra>
        Se nada for digitado, o programa deve imprimir uma mensagem de erro.
    Exiba em caso de erro:
        "Erro: nome inválido."
"""

name = input("Digite seu nome: ")
age = input("Digite sua idade: ")

if name != '' and age != '':
    print(f'Olá, {name}! você tem {age} anos.')
    print(f'Seu nome invertido é {name[::-1]} e sua idade ao contrário é {age[::-1]}') # [::-1] inverte a string
    print(f'Seu nome contém espaços? {name.isspace()}') # isspace() verifica se a string contém espaços
    print(f'Seu nome tem {len(name)} letras.') # len() retorna o tamanho da string
    print(f'Seu nome tem {name.count("a") + name.count("e") + name.count("i") + name.count("o") + name.count("u")} vogais.') # count() conta quantas vezes o caractere aparece na string
    print(f'Seu nome tem {len(name) - (name.count("a") + name.count("e") + name.count("i") + name.count("o") + name.count("u"))} consoantes.') # len() retorna o tamanho da string e count() conta quantas vezes o caractere aparece na string diminuindo o número de vogais
    print(f'Seu nome tem {name.count(" ")} espaços.') # count() conta quantas vezes o caractere aparece na string, nesse caso, espaços
    print(f'A primeira letra do meu nome é {name[0]}') # [0] retorna o primeiro caractere da string
    print(f'A última letra do meu nome é {name[-1]}') # [-1] retorna o último caractere da string
else:
    print("Erro: nome inválido.")
    
    
    
