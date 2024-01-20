'''   
        Introdução ao Try e Except
O try e except são usados para tratar erros no código.
O try funciona como um teste, se o código funcionar, o except não é executado.
Se o código não funcionar, o except é executado.
'''

number_str = input('Digite um número e irei dobrar ')

try:
    number_float = float(number_str)
    print(f'o dobro de {number_str} é {number_float * 2:.2f}')
except:
    print('Erro: não é um número')
    


# if number_str.isdigit():
#     number_float = float(number_str)
#     print(f'o dobro de {number_str} é {number_float * 2:.2f}')
# else:
#     print('Erro: não é um número')
