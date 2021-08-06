if __name__ == '__main__':

    while True:

        try:
            s = input()
            l = len(s)
            aux = 0

            for i in range(len(s)):
                aux = i
                while aux != 0:
                    print('',end=' ')
                    aux-=1

                for j in range(l):
                   if j!= l-1:
                    print(s[j],end=' ')
                   else:
                    print(s[j],end='')

                l-=1
                print('')
            print('')

        except EOFError:
            break
