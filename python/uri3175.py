if __name__ == '__main__':
    count = int(input())
    l = sorted(list(map(int,input().split())))
    aux = 1
    soma = 0

    for i in range(len(l)-1):
        soma+=aux

        if l[i] != l[i+1]:
            aux+=1

    print(soma+aux)