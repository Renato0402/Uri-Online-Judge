if __name__ == '__main__':
    count = int(input())
    for i in range(count):
        s = input().split()

        s1 = s[0]
        s2 = s[1]
        aux = ''

        s1 = s1[::-1]
        s2 = s2[::-1]

        if s1[0:len(s2)].__eq__(s2):

            print('encaixa')
        else:

            print('nao encaixa')
