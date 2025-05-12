palavra = input('Digite a palavra: ')
# o atributo lower desabilita a diferenciação de minusculo e maiusculo do python
palavra = palavra.lower()

texto_modificado = palavra.replace('i', '1').replace('a', '4')
print('Texto modificado', texto_modificado)
