
import math

if __name__ == '__main__':

    while True:
        try:
            flag = False
            flag2 = False
            l = ['0','1','4','6','8','9']
            aux = 0
            n = int(input())

            if n == 1:
                print('Nada')

            else:

             if n == 2 or n == 3:
                print('Super')

             else:

              if n%2==0  or n%3 == 0:
                print('Nada')

              else:
                for j in range(5,int(math.sqrt(n))+1,2):
                    if n%j == 0:
                     aux+=1

                    if aux >= 1:
                        print('Nada')
                        break

                if aux == 0:
                    flag = True


             if flag:
                for i in l:
                    if i in str(n):
                        print('Primo')
                        flag2 = True
                        break

             if not flag2 and flag:
                 print('Super')


        except EOFError:
            break