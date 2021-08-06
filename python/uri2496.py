if __name__ == '__main__':
    count = int(input())
    alfa = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    cont = 0

    for i in range(count):
        l = int(input())
        s = input()
        if alfa[0].__contains__(s):
            print(f'There aren{chr(39)}t the chance.')
            continue

        for j in range(l):
            if s[j] != alfa[0][j]:
                cont+=1

            if cont > 2:
                print(f'There aren{chr(39)}t the chance.')
                break

        if cont <= 2:
            print('There are the chance.')
        cont=0