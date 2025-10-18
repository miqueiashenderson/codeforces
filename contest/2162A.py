testes = int(input())

for i in range(testes):

    length = int(input())
    array = list(map(int, input().split()))

    print(max(array))
