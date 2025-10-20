tst = int(input())

for i in range(tst):

    n, k = map(int, input().split())
    string = input()
    pos = 0
    index = -k - 1

    for i in range(n):

        if string[i] == "1": 

            if i - index  >= k:
                pos += 1

            index = i

    print(pos)

