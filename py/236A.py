#se o número de caracteres distintos no nome de usuário de alguém for ímpar, então ele é do sexo masculino; caso contrário, ela é do sexo feminino.

entrada = input()
diffs = ""

for letra in entrada:
    if letra not in diffs:
        diffs += letra

if len(diffs) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
