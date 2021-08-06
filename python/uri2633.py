if __name__ == '__main__':
  while True:
   try:
    count = int(input())
    v = []

    for x in range(count):
        n = input().split()
        n1 = n[0]
        n2 = int(n[1])
        v.append([n1,n2])

    v.sort(key=lambda x:x[1])

    for i in range(len(v)):
      if i != len(v)-1:
        print(v[i][0],end=' ')
      else:
        print(v[i][0],end='')

    print('')

   except EOFError:
       break