# -*- coding: utf-8 -*-
import math

if __name__ == '__main__':

 f = [200, 20, 30, 50]
 w = [300, 10, 25, 40]
 e = [400, 25, 55, 70]
 a = [100, 18, 38, 60]

 all = [f, 'f', w, 'w', e, 'e', a, 'a']

 count = int(input())
 for x in range(0, count):
    v = []
    entrada = list(map(int, input().split()))
    w = entrada[0]
    h = entrada[1]
    x0 = entrada[2]
    y0 = entrada[3]

    entrada2 = input().split()
    spell = entrada2[0]
    lvl = int(entrada2[1])
    cx = int(entrada2[2])
    cy = int(entrada2[3])

    for y in range(0, len(all)):
        if spell.startswith(str(all[y])):
            v = all[y - 1]
            break
    r = v[lvl]
    ret = [[x0,y0],[x0+w,y0],[x0+w,y0+h],[x0,y0+h]]
    t = False
    t2 = False
    t3 = False

    if x0 <= cx <= x0 + w and y0 <= cy <= y0 + h:
        t = True

    if not t:

        if x0 <= cx <= x0 + w and (cy - r <= y0 <= cy + r or cy - r <= y0+h <= cy + r):
            t2 = True

        if y0 <= cy <= y0 + h and (cx - r <= x0 <= cx + r or cx - r <= x0+w <= cx + r):
            t2 = True

    if not t and not t2:
        for i in range(4):
            if math.sqrt(pow(cx - ret[i][0],2) + pow(cy-ret[i][1],2)) < r:
              t3 = True
              break

    if t or t2 or t3:
        print(v[0])

    else:
        print(0)



