if __name__ == '__main__':
    n = int(input())
    y = 1
    z = 1


    for x in range(n-1,0,-1):


      for c in range(2,x+1):

        if x%c == 0:
         y+=1
        if (x-2)%c == 0:
         z+=1


      if z == 2 and y ==2:
         print(x-2,x)
         break

      y = 1
      z = 1
