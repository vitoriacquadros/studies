"""
    
CPF: 746.824.890-70

Coletar a soma dos 09 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10 

7 4 6 8 2 5 8 9 0
x x x x x x x x x
10 9 8 7 6 5 4 3 2

7 * 10 = 70
4 * 9 = 36
6 * 8 = 48
8 * 7 = 56
2 * 6 = 12
5 * 2 = 20
8 * 4 = 32
9 * 3 = 27
0 * 2 = 0

Soma = 70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

Multiplicar o resultado por 10 

301 * 10 = 3010

Obter o resto da divisão por 11

3010 % 11 = 7

Se o resultado anterior for maior que 9, o dígito verificador será 0
caso contrário, o dígito verificador será o resultado anterior


"""

cpf = '74682489070'
nove_digitos = cpf[:9]

contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
    
digito_1 = ((resultado_digito_1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
    