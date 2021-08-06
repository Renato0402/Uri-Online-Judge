if __name__ == '__main__':
     n = list(map(int,input().split()))

     if n[0] != n[1]:
         print(max(n))
     else:
         print(n[0])

