#Operadores lógicos 
# and(e) or(ou) not(não)
# 
# and - todas condições precisam ser verdadeiras, se qualquer
# valor for considerado falso a expressão inteira será avaliada naquele valor
# são considerados Falsy 0, 0.0, '' e False. Também existe o tipo
# None que é usado para reprsentar um não valor

# # ex.: uso de senha por input do usuário
#     
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')
# 
# senha_permitida = '12345'
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Você entrou')
# else:
#     print('sair')

# Avaliação de curto circuito
# print(True and True and True)
print(True and False and True)
print(True and False)
print(bool(0.0))
print(bool(''))

print(True and 0 and True)