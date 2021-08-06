if __name__ == '__main__':
    count = int(input())
    sin = 0
    sout = 0

    for x in range(count):
        if 10<= int(input())<=20:
            sin+=1
        else:
            sout+=1
    print(sin,'in')
    print(sout,'out')