import math
import sys


if __name__ == '__main__':
    count = int(sys.stdin.readline())

    for i in range(count):
        n = sys.stdin.readline().split()
        a = int(n[0])
        b = int(n[1])
        pa = float(n[2])
        pb = float(n[3])
        age = 0

        while a <= b:

            a = math.floor(a + (a*pa)/100)
            b = math.floor(b + (b * pb)/100)
            age+=1

            if age > 100:
              break

        if age > 100:
            sys.stdout.write('Mais de 1 seculo.' + '\n')
        else:
            sys.stdout.write(str(age)+' anos.\n')