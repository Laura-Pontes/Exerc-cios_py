#uma função que receba uma lista de objetos (onde cada objeto tem um atributo 'nome') e retorne uma nova lista contendo apenas os nomes de cada objeto
pessoas = [
    {'nome': 'Laura', 'idade': 23}, 
    {'nome': 'Lavínia', 'idade': '22'},
    {'nome': 'Emanuel', 'idade': '19'},
    {'nome': 'João', 'idade': '16'}
]
def extrair_Nomes(pessoas):
    nomes = []
    for obj in pessoas:
        nomes.append(obj['nome'])
    return nomes

resultado = extrair_Nomes(pessoas)
print(resultado)
