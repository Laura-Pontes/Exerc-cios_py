#uma função que recebe uma lista e um valor e retorna quantas vezes aparece
#lista utilizada: numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def  contador_Ocorrencias(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    return contador
numprocurado = int(input('Digite um valor para procura-lo na lista: '))
resultado =  contador_Ocorrencias(numeros, numprocurado)
print(f'{numprocurado} aparece {resultado} veze(s) na lista')