

if __name__ == '__main__':

    while True:
        try:
            count = int(input())
            v = [0]*2
            s = list(map(int, input().split()))

            for i in s:
                v[i] += 1

            if v[1]/count >= 2/3:
                print('impeachment')
            else:
                print('acusacao arquivada')

        except EOFError:
            break
