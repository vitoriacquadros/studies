# Flag (bandeira) - Marcar um local 
# None = não valor 
# is e is not = é ou não é (tipo, valor idadentidade) 
# id = Identidade 

# v1 = 'a'
# print(id(v1)) #visualiza a identidade na memória

# v2 = 'a'
# print(id(v2)) 

# v3 = 'b'
# print(id(v3)) 

condicao = True
passou_no_if = None
if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')
    
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)