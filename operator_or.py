# or - qualquer condição verdadeira avalia toda a expressão como verdade.
# Se qualquer valor for verdade a expressão inteira será avaliada naquele valor.
# permitir maisuculo ou minusculo
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '12345'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Você entrou')
else:
    print('sair')
    
#avaliação curto circuito
    
print(0 or False or 0 or 'abc' or True)


senha = input('Senha: ') or 'Sem senha'
print(senha)