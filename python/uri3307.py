import math

if __name__ == '__main__':
    count = int(input())

    for i in range(count):
        n = int(input())
        r = math.sqrt(n/ 12.56)


        if r < 12:
            print('vermelho = R$ {:.2f}'.format(n*0.09))

        if 12 <= r <= 15:
            print('azul = R$ {:.2f}'.format(n*0.07))

        if r > 15:
            print('amarelo = R$ {:.2f}'.format(n*0.05))
