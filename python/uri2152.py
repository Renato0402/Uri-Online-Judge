if __name__ == '__main__':
    count=int(input())

    for x in range(count):
        n = input().split()
        h = n[0]
        m = n[1]
        af = n[2]

        if int(h) < 10:
            h = '0'+h

        if int(m) < 10:
            m = '0'+m

        if af == '1':
            print(f'{h}:{m} - A porta abriu!')
        else:
            print(f'{h}:{m} - A porta fechou!')