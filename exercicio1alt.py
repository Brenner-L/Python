# 1. Pede a palavra
palavra = input('Digite uma palavra  ')

# 2. Cria uma palavra invertida vazia
palavra_invertida = ''

# 3. vai pegando as letras da palvra de trás para frente
for letra in range(len(palavra) -1, -1, -1):
    palavra_invertida += palavra[letra]


if palavra == palavra_invertida:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')