from csv import reader

lista = []

with open('teste.csv', newline='') as arquivo:  # Abrir o arquivo csv
    leitor_csv = reader(arquivo, delimiter=';')
    next(leitor_csv)  # Pular o cabeçalho
    lista = list(leitor_csv)  # Transformar em uma lista
    for i in range(0, len(lista)):
        lista[i][0], lista[i][1] = lista [i][1], lista[i][0]  # Trocar o índice numérico com o nome
    lista.sort()  # Organizar em ordem alfabética

print(lista)
