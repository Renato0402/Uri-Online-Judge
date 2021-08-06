if __name__ == '__main__':
    par = 0
    impar = 0
    pos = 0
    neg = 0
    for i in range(0,5):
        x = int(input())
        if x%2 == 0:
            par+=1
        else:
            impar+=1
        if x >= 0:
          if x != 0:
            pos+=1
        else:
            neg+=1

    print(par,'valor(es) par(es)')
    print(impar, 'valor(es) impar(es)')
    print(pos, 'valor(es) positivo(es)')
    print(neg, 'valor(es) negativo(es)')
