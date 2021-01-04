dic = [
    {
        'nome': 'Guilherme',
        'idade': 19,
        'sexo': 'M'
    },
    {
        'nome': "Nina",
        'idade': 30,
        'sexo': 'F'
    },
    {
        'nome': 'Giovana',
        'idade': 21,
        'sexo': 'F'
    }
]
checagem = None
lista = []

for i in range(0, len(dic)):
    checagem = dic[i].get('nome', 'Não encontrado')  # pegar o nome e devolver 'Não encontrado' se não achar 'nome'
    if checagem != 'Não encontrado':
        lista.append(dic[i]['nome'])  # Se encontrar adicione o nome a lista
    else:
        print(f'chave nome não encontrada na {i+1}° biblioteca')  # Se não encontrar imprima que não encontrou e em qual biblioteca
    for j in range(0, len(lista)-1):
        if (dic[i]['nome']) == lista[j]:  # Checagem para ver se 'nome' existe na biblioteca
            lista.pop()  # Retira o nome da lista se já existir
            print(f"O nome {dic[i]['nome']} já está na lista.")
        else:
            None


print(lista)
