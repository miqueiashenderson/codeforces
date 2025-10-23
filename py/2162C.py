t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    if a.bit_length() < b.bit_length():
        print(-1)
        continue
    
    if a == b:
        print(0)
        continue
    
    x = a ^ b

    if x <= a:
        print(1)
        print(x)
        continue
    
    a1 = a | b
    x1 = a ^ a1
    x2 = a1 ^ b
    print(2)
    print(x1, x2)
