

if __name__ == '__main__':

    z = 1
    while True:
        try:
            n = int(input())
            mul = 1

            if n == 0:
                print('Caso %d: %d numero' % (z, int((((n + 1) * n) / 2) + 1)))
            else:
                print('Caso %d: %d numeros' % (z, int((((n + 1) * n) / 2) + 1)))
            for x in range(0, n + 1):
                print(f'{x} ' * mul, end='')
                if x < 1:
                    mul = 1
                else:
                    mul += 1
            print(" ")
            z += 1


        except EOFError:
            break