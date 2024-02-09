"""
split and join with list and string
split -> divide uma string
join -> junta uma lista de strings
strip() -> corta espaços no começo e no fim
rstrip() -> corta espaços a direita
lstrip() -> corta espaço a esquerda
"""

frase = 'O rato roeu a roupa do rei de roma'
lista_palavras = frase.split()
print(lista_palavras)

lista_frases = []

for i, frase in enumerate(lista_palavras):
    lista_frases.append(lista_palavras[i].strip())
    

print(lista_frases)

frases_unidas = ' , '.join(lista_frases)
print(frases_unidas)
