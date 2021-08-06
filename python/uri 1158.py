if __name__ == '__main__':
     count = int(input())

     for x in range(0,count):
         n = list(map(int,input().split()))
         if n[0]%2 == 0:
             soma = n[0]+1
         else:
             soma = n[0]

         prox = soma
         for y in range(1,n[1]):
           prox+=2
           soma+=prox

         print(soma)