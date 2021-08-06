if __name__ == '__main__':
    count = int(input())
    v = []
    for i in range(count):
        v.append(input())

    aux = 0
    for i in range(0,len(v)):
        for j in range(i+1,len(v)):
            if v[i][0][0] >= v[j][0][0]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux

    for i in range(0,len(v)):
        for j in range(i+1,len(v)):
            if v[i][0][0] == v[j][0][0]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux

    print('\n'.join(v))

