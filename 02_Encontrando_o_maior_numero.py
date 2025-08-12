#Uma função que recebe uma lista de números e retorna o maior
#lista utilizada: numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def maior_Numero(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior
resultado = maior_Numero(numeros)
print(resultado, 'É o maior da lista')

