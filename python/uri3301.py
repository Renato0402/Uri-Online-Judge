if __name__ == '__main__':
    n = list(map(int,input().split()))
    pos = 0
    v = ['huguinho','zezinho','luisinho']

    for x in range(len(n)):
        if n[x]!=max(n) and n[x]!= min(n):
            pos = x
    print(v[pos])

