tests = int(input())
        
for i in range(tests):
    tamanho = int(input())
    string = input()
       
    x = []
        
    for j in range(tamanho):
        if string[j] == "1":
            x.append(j + 1)
     
    print(len(x))
     
    print(" ".join(map(str, x)))
