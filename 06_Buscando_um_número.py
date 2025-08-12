#a função recebe um numero e uma lista one busca o número e retorna True ou False
#lista utilizada: numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
numero = int((input('Digite um número inteiro para buscar na lista: ')))
def busca(numero, lista):
    for item in lista:
        if item == numero:
            return True
    return False
resultado = busca(numero,numeros)
print(resultado)