if __name__ == '__main__':
    while True:
        n = list(map(int,input().split()))
        n1 = n[0]
        n2 = n[1]

        if n1 == 0 or n2 == 0:
            break

        if n1>0 and n2 > 0:
            print('primeiro')

        if n1< 0 and n2> 0:
            print('segundo')

        if n1< 0 and n2 <0:
            print('terceiro')

        if n1> 0 and n2<0:
            print('quarto')