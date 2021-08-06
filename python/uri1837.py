if __name__ == '__main__':
    entrada = list(map(int,input().split()))
    q = 0
    r = 0
    x = entrada[0]

    if entrada[0] >= 0:

     while x + (entrada[1]*q) > 0:
        entrada[0] -= abs(entrada[1])
        if entrada[0] < 0:
            break
        q += 1

     if entrada[1] > 0:
      r = x - (entrada[1] * q)
     else:
      r = x + (entrada[1] * q)

    else:
     entrada[0] = abs(entrada[0])
     while entrada[0] > 0:

      q-=1
      entrada[0]-=abs(entrada[1])

     if entrada[1] > 0:
         r = x - (entrada[1] * q)
     else:
         r = x + (entrada[1] * q)

    if entrada[1] > 0:
      print(q,r)
    else:
      print(-q,r)