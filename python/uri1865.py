if __name__ == '__main__':
    count = int(input())

    for x in range(count):
        n = input().split()
        if n[0] == 'Thor':
            print('Y')
        else:
            print('N')