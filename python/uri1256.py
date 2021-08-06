if __name__ == '__main__':
 count = int(input())


 for x in range(count):
    n = input().split()
    div = int(n[0])
    qtd = int(n[1])
    table = [] * div
    v = list(map(int, input().split()))
    for i in range(div):
        table.append([] * div)

    for i in v:
        table[i % div].append(i)

    for i in range(len(table)):
        if len(table[i]) == 0:
            print(f'{i} -> {chr(92)}')
        else:
            if i == 0:
                print('')
            for j in range(len(table[i])):
                if j == 0:
                 print(f'{i} -> {table[i][j]}', end=' ')
                else:
                    print(f'-> {table[i][j]}', end=' ')

            print(f'-> {chr(92)}')


