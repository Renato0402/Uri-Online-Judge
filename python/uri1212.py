if __name__ == '__main__':

    while True:
        c = 0
        cont = 0
        flag = False
        n = input().split()
        n1 = n[0]
        n2 = n[1]

        if n1 == '0' and n2 == '0':
            break

        if len(n1) > len(n2):
            aux = n1
            n1 = n2
            n2 = aux

        l = len(n2) - 1

        for i in range(len(str(n1)) - 1, -1, -1):

            if int(n1[i]) + int(n2[l]) + c > 9:
                cont += 1
                c = 1
            else:
                c = 0
            l -= 1

        dif = len(str(n2)) - len(str(n1)) - 1

        while dif >= 0:
            flag = False
            if int(n2[dif]) + c > 9:
                cont += 1
                flag = True

            if not flag:
                break

            dif -= 1



        if cont == 0:
            print('No carry operation.')

        if cont == 1:
            print(f'{cont} carry operation.')

        if cont >= 2:
            print(f'{cont} carry operations.')
