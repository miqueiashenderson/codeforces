import math

entrada = input().split()
n, m, a = int(entrada[0]), int(entrada[1]), int(entrada[2])

x = math.ceil(m/a)
y = math.ceil(n/a)

resultado = x * y

print(resultado)
