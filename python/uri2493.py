if __name__ == '__main__':
    while True:
        try:
            count = int(input())
            ex = []
            ex2 = []
            p = []
            ii = []

            for i in range(count):
                n = input().strip().split()
                ex.append(n)
                ex2.append(n[1].split('='))

            for i in range(count):
                n = input().strip().split()
                p.append(n)

            for i in range(0,len(p)):
                n1 = int(ex[int(int(p[i][1]))-1][0])
                n2 = int(ex2[int(int(p[i][1])-1)][0])
                r = int(ex2[int(int(p[i][1])-1)][1])

                if p[i][2] == 'I':
                    if n1 + n2 == r or n1 * n2 == r or n1 - n2 == r:
                        ii.append(p[i][0])

                if p[i][2] == '+':
                    if n1 + n2 != r:
                        ii.append(p[i][0])

                if p[i][2] == '-':
                    if n1 - n2 != r:
                        ii.append(p[i][0])

                if p[i][2] == '*':
                    if n1 * n2 != r:
                        ii.append(p[i][0])

            if len(ii) == 0:
                print('You Shall All Pass!')

            if len(ii) == len(p):
                print('None Shall Pass!')

            ii = sorted(ii)
            if 0 < len(ii) < len(p):
                for i in range(len(ii)):
                    if i != len(ii)-1:
                        print(ii[i],end=' ')
                    else:
                        print(ii[i])

        except EOFError:
            break
