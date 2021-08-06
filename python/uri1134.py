if __name__ == '__main__':
    somaA = 0
    somaG = 0
    somaD = 0
    t = int(input())
    while t!=4:
        if t== 1:
            somaA += 1
        if t == 2:
            somaG += 1
        if t == 3:
            somaD += 1
        t = int(input())

    print('MUITO OBRIGADO')
    print('Alcool:', somaA)
    print('Gasolina:', somaG)
    print('Diesel:', somaD)
