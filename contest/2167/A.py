test = int(input())

for _ in range(test):
    a, b, c, d = map(int, input().split())

    if a != b or a != c or a != d:
        print("NO")
    else:
        print("YES")

