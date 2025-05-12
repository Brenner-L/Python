def codificar_cesar(texto, deslocamento=3):
    resultado = ''
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nova_letra = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += nova_letra
        else:
            resultado += char #Mantém espaços e pontuação
    return resultado

#Exemplo de uso
entrada = input('Digite a mensagem a ser codificada')
codificada = codificar_cesar(entrada)
print('Mensagem codificada:', codificada)
