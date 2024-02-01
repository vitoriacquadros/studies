condicao = True

while condicao:
    nome = input('Digite seu primeiro nome: ')
    print('Seu nome é:', nome)
    
    if nome == 'sair':
        break #para o loop
print( 'Acabou o programa!')


# =================================================================================
contador = 0 

while contador <= 100:
    contador += 1
    
    if contador == 6:
        print('O número 6 é chato!')
        continue
    
    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue
        
    print(contador)
    
    if contador == 40:
        break
    
print('Acabou o programa!')

#======================================================================================

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1 
    while coluna <= qtd_colunas:
        print(coluna, end=' ')
        coluna += 1

    
    linha += 1
