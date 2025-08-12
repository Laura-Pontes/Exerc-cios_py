#uma função que recebe uma lista e retorna outra na ordem contraria
#lista utilizada: numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def lista_Inversa(lista):
    invertida = lista[::-1]
    return invertida
resultado = lista_Inversa(numeros)
print(resultado)