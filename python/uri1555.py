


def rafael(x,y):
    return (3*x)**2 + y**2

def beto(x,y):
    return 2*(x)**2 + (5*y)**2

def carlos(x,y):
    return -100*x + y**3

entrada = input()

for i in range(0,int(entrada)):

 input2 = input()
 numero = input2.split(" ")

 x = 0
 y = 0




 try:
     y = int(numero[1])
     x = int(numero[0])
 except IndexError:
     pass

 if rafael(x,y) > beto(x,y) and rafael(x,y) > carlos(x,y):
    print("Rafael ganhou")
 if beto(x,y) > rafael(x,y) and beto(x,y) > carlos(x,y):
    print("Beto ganhou")
 if carlos(x,y) > beto(x,y) and carlos(x,y) > beto(x,y):
    print("Carlos ganhou")