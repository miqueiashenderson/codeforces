n = int(input())
count = 0
for i in range(n):
    entrada = input().split()
    soma = int(entrada[0]) + int(entrada[1]) + int(entrada[2])
    if soma >= 2:
        count += 1


print(count)
