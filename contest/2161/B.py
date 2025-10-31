test = int(input())

for _ in range(test):

    n = int(input())
    tabela = []

    for i in range(n):
        linha = input()
        tabela.append(linha)

    booleano = True
    for i in range(n):
        if "###" in tabela[i]:
            booleano = False
            break

    for j in range(n):
        coluna = ""
        for i in range(n):
            coluna += tabela[i][j]

        if "###" in coluna:
            booleano = False
            break

    if booleano:
        print("YES")
    else:
        print("NO")

