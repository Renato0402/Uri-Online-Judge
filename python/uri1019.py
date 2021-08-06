if __name__ == '__main__':
    n = int(input())
    h = 0
    m = 0
    while n > 3600:
        h+=1
        n = n-3600


    while n > 60:
        m+=1
        n = n-60
    print(f'{h}:{m}:{n}')



