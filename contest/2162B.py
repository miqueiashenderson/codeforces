casos_de_teste = int(input())

for _ in range(casos_de_teste):
    n = int(input())
    s = input()

    solucao_encontrada = False
    for i in range(1 << n):
        p_caracteres = []
        p_indices = []
        x_caracteres = []

        for j in range(n):
            if (i >> j) & 1:
                p_caracteres.append(s[j])
                p_indices.append(j + 1)
            else:
                x_caracteres.append(s[j])

        if p_caracteres != sorted(p_caracteres):
            continue

        if x_caracteres != x_caracteres[::-1]:
            continue

        print(len(p_indices))
        print(*p_indices)
        solucao_encontrada = True
        break

    if not solucao_encontrada:
        print(-1)
