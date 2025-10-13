n_str, k_str = input().split()
n = int(n_str)
k = int(k_str)

pontuacoes_str = input().split()

pontuacoes = []
for p_texto in pontuacoes_str:
    pontuacoes.append(int(p_texto))

pontuacao_de_corte = pontuacoes[k - 1]

avancaram = 0

for pontuacao_atual in pontuacoes:
    if pontuacao_atual >= pontuacao_de_corte and pontuacao_atual > 0:
        avancaram += 1

print(avancaram)
