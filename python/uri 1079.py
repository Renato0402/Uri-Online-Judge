if __name__ == '__main__':
    count = int(input())
    for x in range(count):
        n = list(map(float,input().split()))
        print('{:.1f}'.format((n[0]*2 + n[1]*3 + n[2]*5)/10))