"""_summary_ CORRIGIR ESTE CÓDIGO

Ex9.: Faça uma lista de compras com listas 
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista 
não permita que o programa quebre com erros de índices inexistentes na lista
"""

shopping_list = []

while True: 
    insert = input('Selecione uma opção: \n1 - Adicionar produto\n2 - Remover produto\n3 - Listar produtos\n4 - Sair\n')
    if insert == '1':
        a = input('Digite o nome do produto que deseja adicionar a lista de compras: ')
        shopping_list.append(a)
    elif insert == '2':
        d = input('Digite o nome do produto que deseja remover da lista de compras: ')
        shopping_list.remove(d)
        if d not in shopping_list:
            print('Produto não encontrado na lista de compras')
    elif insert == '3':
        for i in range(len(shopping_list)):
            print(i, shopping_list[i])

    elif insert == '4':
        break
    else:
        print('Opção inválida')
        
        
        
        
    # a = input('Digite o nome do produto que deseja adicionar a lista de compras: ')
    # shopping_list.append(a)
    # b = input('Deseja adicionar mais algum produto? (s/n) ')
    # if b == 'n':
    #     break
    # elif b == 's':
    #     continue
    # c = input('Deseja remover algum produto? (s/n) ')
    # if c == 's':
    #     d = input('Digite o nome do produto que deseja remover da lista de compras: ')
    #     shopping_list.remove(d)
    # elif c == 'n':
    #     continue

