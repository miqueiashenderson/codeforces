entrada = input()

cont_lower = 0
cont_upper = 0

for letra in entrada:
    if letra.islower():
        cont_lower += 1
    else:
        cont_upper += 1

if cont_upper > cont_lower:
   print(entrada.upper())

elif cont_lower > cont_upper:
   print(entrada.lower())

else:
    print(entrada.lower())
    

