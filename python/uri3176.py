if __name__ == '__main__':
    count = int(input())
    v = []

    for i in range(count):
        s = input().split()
        v.append([s[0],s[1]])

    v = sorted(v, key=lambda x: (x[0]))
    v = sorted(v,reverse=True, key=lambda x: (x[1]))
    qtd = int(count/3)

    for i in range(qtd):
        print(f'Time {i+1}')
        for j in range(i,len(v),qtd):
            print(v[j][0],v[j][1])
        print('')
