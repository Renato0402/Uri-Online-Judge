if __name__ == '__main__':
    entrada = input().split()
    dif = int(entrada[0])
    count = int(entrada[1])
    d = 0
    t = []
    for i in range(count):
        v = input().split()
        left = v[0][0:2]
        right = v[0][3:]
        if left == '23':
            d+=60
        d-=int(right)

        if abs(d)<=dif:
            if left =='23':
             t.append([v[1],int(left+right)])

            else:
                t.append([v[1], int(left + right)+2400])

        d=0

    t = sorted(t,key=lambda x:(x[1]))

    for i in t:
        print(i[0])