if __name__ == '__main__':
    entrada = input().split()
    l = int(entrada[0])
    c = int(entrada[1])
    v = []

    for i in range(l):
        v.append(input().split())

    v1 = []
    d = []

    for i in range(l):
        for j in v[i]:
          if j.__contains__('V'):
            v1.append(j[0])
          else:
            d.append(j[0])

    v1.sort(reverse=True)
    d.sort(reverse=True)

    for i in v1:
        print(f'{i}V')

    for i in d:
        print(f'{i}D')
