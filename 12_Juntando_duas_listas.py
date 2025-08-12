#uma função que recebe duas listas e retorna outra com a junção delas
#lista utilizada natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
#lista utilizada tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]
natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]
def junta_Listas(lista1, lista2):
    concatenação = lista1 + lista2
    return concatenação
resultado = junta_Listas(natureza, tecnologia)
print(resultado)