# 1. Pede para o usuario digitar uma palavra
palavra = input('Digite uma palavra')

# 2. Inverte a palavra usando um truque do python
palavra_invertida = palavra[::-1]

# 3. Comprara a palavra original com a invertida
if palavra == palavra_invertida:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')    
