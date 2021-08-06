
import math

if __name__ == '__main__':
 dic = {'W':1,'H':1/2, 'Q':1/4, 'E':1/8, 'S':1/16,'T':1/32, 'X':1/64}
 while True:
    t = input().strip().split('/')
    if t[0] == '*':
        break
    c = 0
    cont = 0
    for i in t:
        for j in i:
            if j in dic.keys():
              c+=dic.get(j)

        if c == 1:
            cont+=1
        c = 0

    print(cont)
