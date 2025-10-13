n = int(input())
s = input()
cont = 0

for i in range(n - 1):
    if s[i] == s[i + 1]: 
        cont += 1

print(cont)
