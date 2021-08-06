import sys

if __name__ == '__main__':

    t = 1

    while True:

        count = int(sys.stdin.readline())

        if count == 0:
            break

        if count != 0 and t != 1:
            print('')

        print(f'Instancia {t}')

        c = int(count * ((count - 1) / 2))
        v = []

        for i in range(count):
            v.append([0.0] * 4)

        for i in range(c):
            n = list(map(int, sys.stdin.readline().split()))
            ta = n[0] - 1
            tb = n[2] - 1
            pa = n[1]
            pb = n[3]

            if pa > pb:
                v[ta][0] += 1

            else:
                v[tb][0] += 1


            v[ta][2] += pa
            v[ta][3] += float(pb)

            v[tb][2] += pb
            v[tb][3] += float(pa)

            v[ta][1] = ta + 1
            v[tb][1] = tb + 1

        for i in range(count):
            if v[i][3] != 0:
             v[i][3] = v[i][2] / v[i][3]


        v = sorted(v, reverse=True, key=lambda x: (x[0], x[3], x[2]))

        for i in range(len(v)):
            for j in range(i + 1, 3):
                if v[i][0] < v[j][0]:
                    if v[i][2] == v[j][2] and v[i][3] == v[i][3]:
                        aux = v[i]
                        v[i] = v[j]
                        v[j] = v[i]

        for i in range(len(v)):

            if i != len(v) - 1 and v[i][1] != 0:
                print(str(v[i][1]), end=' ')

            if i == len(v) - 1 and v[i][1] != 0:
                print(str(v[i][1]))


        t += 1
