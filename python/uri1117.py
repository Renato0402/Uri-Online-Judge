if __name__ == '__main__':
    t = []
    while True:
     n = float(input())
     if n <= 10 and n>=0:
         t.append(n)
     else:
         print('nota invalida')

     if len(t) == 2:
         break

    print('media = {:.2f}'.format((t[0]+t[1])/2))