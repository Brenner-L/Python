p1 = input('Digite a primeira palavra ')
p2 = input('Digite a segunda palavra ')
p3 = input('Digite a terceira palavra ')
p4 = input('Digite a quarta palavra ')
p5 = input('Digite a quinta palavra ')

#armazenar cada variavel de p1 a p5 na lista palavras

palavras = [p1, p2, p3, p4, p5]

#ordena a lista em ordem alfabética através do atributo sort
palavras.sort()

#mostra as palavras já ordenadas
print('Palavras em ordem alfabética')
for palavra in palavras:
    print(palavra)
    