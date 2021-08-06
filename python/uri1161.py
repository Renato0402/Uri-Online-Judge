if __name__ == '__main__':

    while True:
        try:
         entrada = list(map(int,input().split()))
         m = entrada[0]
         n = entrada[1]

         fatN = 1
         fatM = 1

         for i in range(1,m+1):

             fatM*=i

         if m!=n:
           for i in range(1,n+1):
             fatN*=i

         if m!=n:
             print(fatM+fatN)
         else:
             print(fatM+fatM)



        except EOFError:
            break
