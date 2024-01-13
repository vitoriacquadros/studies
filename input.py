# coleta de dados do usuário
# o valor de input armazena na variavél criada

nome = input('qual o seu nome? ')

numero_1 = input('Digite um número: ')

numero_2 = input('Digite outro numero')

# ou
# neste trecho será possível fazer a checagem do número
# quando adicionado type direto no input poderá dar erro na hora de trabalhar com determinado dado


int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

soma = int_numero_1 + int_numero_2

print(f'O seu nome é {nome}')
print(f'A soma dos números que você digitou é igual a {soma}')


