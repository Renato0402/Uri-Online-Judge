if __name__ == '__main__':

 while True:
  try:
    count = int(input())
    v = []

    for i in range(count):
        s = input().split()
        v.append([s[0],s[1],int(s[2])])
    v = sorted(v,key=lambda x:(x[2],x[1],x[0]))

    for i in range(0,len(v)):
        print(v[i][0])

  except EOFError:
      break