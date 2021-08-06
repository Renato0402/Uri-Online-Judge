import sys
from collections import defaultdict
import os

if __name__ == '__main__':

    count = int(input())

    for i in range(count):
        dic = defaultdict(int)

        c = input()
        v = sys.stdin.readline().split()
        for j in v:
            dic[int(j)]+=1

        t = sorted(dic)

        for j in t:
            for k in range(dic[j]):
                sys.stdout.write(str(j)+' ')
        print('')




