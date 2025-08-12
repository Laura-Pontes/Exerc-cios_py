#uma função que recebe uma lista e retorna a soma dos valores
#lista utilizada: numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def soma_Numeros(lista):
    soma = 0 
    for valores in numeros:
        soma += valores
    return soma
resultado = soma_Numeros(numeros)
print('A soma dos valores da lista é de:', resultado)