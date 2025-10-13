n = int(input())
count = 0
for i in range(n):
    operation = str(input())
    for j in range(len(operation)-1):
        if operation[j] == "+" and operation[j+1] == "+":
            count += 1
        elif operation[j] == "-" and operation[j+1] == "-":
            count -= 1

print(count)
