if __name__ == '__main__':
    amount = int(input())
    l = list(map(int,input().split()))
    n1 = l[0]
    n2 = l[1]

    if n1 + n2 > amount:
        print('Deixa para amanha!')
    else:
        print('Farei hoje!')