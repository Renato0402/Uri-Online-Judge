if __name__ == '__main__':
    count = int(input())
    for a in range(0,count):
        n = input().split()
        x = int(n[0])
        y = int(n[1])
        if y != 0:
            print('{:.1f}'.format(x/y))
        else:
            print('divisao impossivel')
