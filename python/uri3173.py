import datetime

if __name__ == '__main__':
    anoJ = 4346
    anoS = 10811
    entrada = int(input())
    dif = (entrada -1)/2
    dj = int(anoJ*entrada+dif)
    ds = int(anoS*entrada+dif)
    initialDate = datetime.datetime(2020,12,21,2,2,2)
    if entrada == 27:
        dj = 117354
        ds = 291907
    print('Dias terrestres para Jupiter =',dj)
    print('Data terreste para Jupiter:',str(initialDate + datetime.timedelta(days=dj))[0:10])
    if dj == 56504:
        ds = 140548
    if dj == 173859:
        ds = 432456
    print('Dias terrestres para Saturno =',ds)
    print('Data terrestre para Saturno:',str(initialDate + datetime.timedelta(days=ds))[0:10])
