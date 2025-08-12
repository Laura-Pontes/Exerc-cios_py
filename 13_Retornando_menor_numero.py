#uma função que recebe uma lista e retorna o maior valor
#lista utilizada: numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def menor_Valor(lista):
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor
    return menor
resultado = menor_Valor(numeros)
print(resultado)