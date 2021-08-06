import math
PI = 3.1415926535897932384626433832795

while True:
    try:
     n = input().split(" ");
     answer = 5*(math.tan(PI*float(n[0])/180)*float(n[1]) + float(n[2]))
     print(str(round(answer,2)))

    except EOFError:
        break