
import math

if __name__ == '__main__':
    while True:
        try:

         entrada = list(map(float,input().split()))
         a = entrada[0]
         d = entrada[1]
         r = entrada[2]

         tan = math.tan(math.pi*(r-90)/180)

         print('{:.4f}'.format(a+tan*d))


        except EOFError:
            break