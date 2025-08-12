#uma função que recebe uma lista com valores duplicados e retorna outra com valores unicos
#lista utilizada: numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def removendo_Duplicatas(lista):
    valores_unicos = []
    for valor in lista:
        if valor not in valores_unicos:
            valores_unicos.append(valor)
    return valores_unicos
resultado = removendo_Duplicatas(numeros)
print(resultado)