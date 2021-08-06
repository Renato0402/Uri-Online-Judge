if __name__ == '__main__':
    count = int(input())
    v = []
    l = 0
    for i in range(4):
        v.append([])

    while count != 0:
        i = input()
        while not i.__contains__('-') and i != '0':
            l+=1
            v[abs(count+1)].append(i)
            i = input()

        count = int(i)

    # oeste,norte,sul,leste
    aux = v[1]
    v[1] = v[2]
    v[2] = aux
    t = True
    while t:
     t = False

     for i in range(len(v)):
        for j in range(len(v[i])):

            if l!= 1:
             print(v[i][j],end=' ')
            else:
             print(v[i][j], end='')
            l-=1

            t = True
            del(v[i][j])
            break
    print('')
