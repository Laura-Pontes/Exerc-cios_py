#uma função que recebe uma lista e calcula a média
#lista utilizada: numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def media_Lista(lista):
    soma = sum(lista)
    unidades = len(lista)
    media = soma/unidades
    return media
resultado = media_Lista(numeros)
print(f'A média dos números da lista é: {resultado}')