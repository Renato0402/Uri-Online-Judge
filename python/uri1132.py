if __name__ == '__main__':
    n1 = int(input())
    n2 = int(input())
    soma = 0
    aux = n1

    if n1 > n2:
        n1 = n2
        n2 = aux

    for x in range(n1,n2+1):
        if x%13 != 0:
            soma+=x
    print(soma)