def meu_bubble_sort(lista_de_numeros_como_string):
    lista_ordenada = lista_de_numeros_como_string[:] 
    n = len(lista_ordenada)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j] > lista_ordenada[j+1]:
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j+1], lista_ordenada[j]
                
    return lista_ordenada

soma_inicial = input()

numeros = soma_inicial.split('+')

numeros_ordenados = meu_bubble_sort(numeros)

soma_final = ""
tamanho_da_lista = len(numeros_ordenados)

for i in range(tamanho_da_lista):
    soma_final += numeros_ordenados[i]
    if i < tamanho_da_lista - 1:
        soma_final += "+"
print(soma_final)
