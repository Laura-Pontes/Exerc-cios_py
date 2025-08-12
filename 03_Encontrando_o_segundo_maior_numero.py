#criar uma função que encontra o segundo maior número da lista sabendo que a lista pode ter numeros duplicados
#lista utilizada: numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def segundo_Maior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    segundo_maior = None
    for num in lista:
        if num < maior and (segundo_maior is None or num > segundo_maior):
            segundo_maior = num
    return segundo_maior
resultado = segundo_Maior(numeros)
print(resultado, 'É o segundo maior')        