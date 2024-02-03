"""Word secret
    Faça um jogo para o usuário adivinhar qual a palavra secreta
    - Você vai propor uma palavra secreta qualquer
    - O usuário vai tentar adivinhar a palavra (apenas uma letra)
    - verificar se contém a letra digitada na palavra secreta
    - Se contiver, mostrar a letra na palavra secreta
    - Se não contiver, mostrar uma mensagem de erro
    - Faça a contagem de tentativas do seu usuário
"""

word = 'python'
secret = list('_'*len(word)) #cria uma lista com o tamanho da palavra secreta
tentativas = 0 #contador de tentativas
while True:
    letter = input('Digite uma letra: ')
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]: #se a letra digitada for igual a letra da palavra secreta
                secret[i] = letter #substitui o underline pela letra digitada
        print(secret)
    else:
        print('Letra não encontrada')
    tentativas += 1
    if ''.join(secret) == word: #se a palavra secreta for igual a palavra digitada. Join junta os elementos da lista secret
        print(f'Parabéns, você acertou a palavra {word} com {tentativas} tentativas')
        break #para o laço se a palavra for acertada
    print(f'Você já tentou {tentativas} vezes')
    print('Tente novamente')