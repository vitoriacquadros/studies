# not - usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')
    
 
#in e not in - strings são iteráveis
# 0 1 2 3 4 5 
# V i t ó r i a 
# 6- 5- 4- 3- 2- 1

nome = 'Vitória'

print('ó' not in nome)

nome = input('Digite o seu nome')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')