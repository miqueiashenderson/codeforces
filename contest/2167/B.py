t = int(input())

for _ in range(t):
    n = int(input())

    s, t = input().split()
    
    cont_s = []

    for letra in s:
        cont_s += letra

    cont_t = []

    for letra in t:
        cont_t += letra
    
    out = ""
    
    tt = sorted(cont_t)
    ss = sorted(cont_s)


    for i in range(n):
        if ss[i] != tt[i]:
            out = "NO"
            break
        else:
            out = "YES"

    print(out)
