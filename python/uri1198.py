if __name__ == '__main__':
    while True:
        try:
            c = list(map(int,input().split()))
            if c[0] < c[1]:
                aux = c[0]
                c[0] = c[1]
                c[1] = aux

            print(c[0] - c[1])

        except EOFError:
            break