if __name__ == '__main__':
    c = int(input())


    for i in range(c):
        k = int(input())
        names = input().split()
        att = input().split()
        contP = 0
        size = 0
        first = True

        for j in range(k):
            for kk in range(len(att[j])):
                size+=1
                if att[j][kk] == 'P':contP+=1
                if att[j][kk] == 'M':size-=1

            if contP/size < 0.75:
              if not first:
                print("",names[j],end='')
              else:
                print(names[j],end='')
                first = False

            contP = 0
            size = 0

        first = True
        print()