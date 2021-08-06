import math

if __name__ == '__main__':
    entrada1 = input().split()
    entrada2 = input().split()
    x1 = float(entrada1[0])
    y1 = float(entrada1[1])
    x2 = float(entrada2[0])
    y2 = float(entrada2[1])
    print('{:.4f}'.format(math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))))