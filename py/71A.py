n = int(input())
out = []

for i in range(n):
    palavra = str(input())
    if len(palavra) <= 10:
        out.append(palavra)
    else:
        abrev = len(palavra) - 2
        out.append(palavra[0] + str(abrev) + palavra[-1])

for i in range(len(out)):
    print(out[i])
