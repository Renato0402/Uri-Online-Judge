if __name__ == '__main__':
    line = int(input())
    column = int(input())
    il = False
    ic = False
    if line%2 == 0:
        il = True
    if column%2 == 0:
        ic = True

    if ic and il or not ic and not il:
        print('1')
    else:
        print('0')