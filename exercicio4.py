texto = input('Digite uma palvra ou frase:')

caractere = input('Digite um caractere que deseja procurar:')

#Verifica se o usuario digitou apenas um caractere
if len(caractere) != 1:
    print('Por favor, digite apenas um caractere')
else:
    print(f'O caractere aparece naa posição:')

#percorre a string e mostra as posições
for i in range(len(texto)):
    if texto[i] == caractere:
        indice=i+1
        print(indice)

       
