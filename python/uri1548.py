if __name__ == '__main__':
    count = int(input())
    j = 0
    v = []

    for i in range(count):
        c = input()
        n = list(map(int,input().split()))
        x = sorted(n,reverse=True)
        for i in range(len(n)):
            if n[i]!=x[i]:
                j+=1
        v.append(str(len(n)-j))
        j=0

    print('\n'.join(v))
