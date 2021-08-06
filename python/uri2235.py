if __name__ == '__main__':
    entrada = list(map(int,input().split()))

    if entrada[0] + entrada[1] == max(entrada)\
        or entrada[0] + entrada[2] == max(entrada)\
        or entrada[2] + entrada[1] == max(entrada):
        print('S')

    elif entrada[0] == entrada[1] or entrada[1] == entrada[2]\
        or entrada[0] == entrada[2]:
        print('S')
    else:
        print('N')