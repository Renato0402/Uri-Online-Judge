if __name__ == '__main__':
    count = int(input())
    ovelhas = list(map(int, input().split()))
    soma,ataques = 0,0
    first = True


    for i in range(0,len(ovelhas)):
       soma+=ovelhas[i]
       if ovelhas[i] % 2 == 0 and first:
            ataques = i + 1
            if ovelhas[0]-1 == 0:
                soma -= i * 2
            else:
                soma -= i*2+ 1

            first = False

    if ataques == 0:
         ataques = count
         soma-=count
    



    print(ataques,soma)
