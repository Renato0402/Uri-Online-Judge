if __name__ == '__main__':
    x = int(input())
    first = True
    c = 0
    if x%2 == 0:
        c = 6
    else:
        print(x)
        c = 5

    for i in range(c):

      if not first:
         print(x+2)
         x+=2

      if x%2 != 0 and first:
          print(x+2)
          x+=2

      if x % 2 == 0 and first:
          print(x+1)
          x+=1

      first = False


