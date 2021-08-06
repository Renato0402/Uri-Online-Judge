if __name__ == '__main__':
    entrada = sorted(list(map(float,input().split())))
    a = entrada[2]
    b = entrada[1]
    c = entrada[0]
    t = False

    if a >= b+c:
        print('NAO FORMA TRIANGULO')
    elif a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    else:
     if a ** 2 > b ** 2 + c ** 2:
        print('TRIANGULO OBTUSANGULO')
     if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')
     if a == b == c:
        print('TRIANGULO EQUILATERO')
        t = True
     if (a == b or a == c or b == c) and not t:
        print('TRIANGULO ISOSCELES')
