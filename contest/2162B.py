tst = int(input())

for i in range(tst):

    n = int(input())
    s = list(input())
    x = ""
    p = ""
    cont = 0

    for i in range(len(s) -1, -1, -1):
        x += str(s[i])
    print(x)

    for i in range(n):
        if x[i] != s[i]:
            p += str(i)
            cont += 1
        
    print(cont)
    print(p)

