if __name__ == '__main__':

    while True:
     entrada = input().split()
     n1 = int(entrada[0])
     n2 = int(entrada[1])
     if n1 == 0 and n2 == 0:
         break
     print(n1*n2)