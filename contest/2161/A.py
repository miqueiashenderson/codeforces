tst = int(input())

for _ in range(tst):
    
    r0, x, d, n = map(int, input().split())

    #div1 aumenta o rating de todos os participantes
    #div2 aumenta o rating dos participantes com o rating estritamente menor x e não aumenta para o resto
    string = input()
    
    rating = r0

    rodadas = 0

    for rodada in string:
    
        aumenta_rating = False
        
        if rodada == "1":
            aumenta_rating = True

        elif rodada == "2":
            
            if rating < x:
                aumenta_rating = True


        if aumenta_rating:

            rodadas += 1

            novo_rating = rating - d

            if novo_rating < 0:
                rating = 0

            else:
                rating = novo_rating

    print(rodadas)




