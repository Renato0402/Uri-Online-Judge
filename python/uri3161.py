if __name__ == '__main__':
    entrada = list(map(int, input().split()))
    fruits = []
    names = []
    c = set()
    nc = []
    check = False
    for x in range(0, entrada[0]):
        fruits.append(input().lower())
    for y in range(0, entrada[1]):
        names.append(input().lower())
    for i in fruits:
        check = False
        for j in names:
            if j.__contains__(i) or j.__contains__(i[::-1]):
                c.add(i)
                check = True
        if check == False:
            nc.append(i)


    for i in fruits:
        if i in c:
            print('Sheldon come a fruta', i)
        else:
            print('Sheldon detesta a fruta', i)
