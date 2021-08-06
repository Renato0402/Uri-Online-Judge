if __name__ == '__main__':
    entrada = int(input())
    for x in range(2,entrada+1,2):
        print(x,end='')
        print('^2 =',x**2)