if __name__ == '__main__':
    while True:
            tamanho = int(input())

            if tamanho == 0:
             break

            n = 2
            m = []
            ii = 1
            jj = 1
            for i in range(tamanho):
                m.append([1]*tamanho)

            for i in range(ii,tamanho-1):
                for j in range(jj,tamanho-1):
                    m[i][j] = n

                n+=1
                ii=0

            print(m)
