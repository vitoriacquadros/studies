nome: str  = 'Ada'
sobrenome: str  = 'Lovelace'
idade: int = 209
ano_atual: int = 2024
ano_nascimento: int = ano_atual - idade
maior_de_idade: bool = idade >= 18
altura_metros: float  = 1.60

print('Nome:', nome) #str
print('Sobrenome:', sobrenome) #str
print('Idade:', idade) #int
print('Ano de nascimento:', ano_nascimento) #int
print('É maior de idade? ', maior_de_idade) #bool
print('Altura em metros:  ', altura_metros) #float

print(f"{nome} no ano de {ano_atual} teria {idade} anos e nasceu em {ano_nascimento}")