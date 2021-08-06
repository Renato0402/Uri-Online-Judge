if __name__ == '__main__':
    entrada = list(map(int,input().split()))
    ih = entrada[0]
    im = entrada[1]
    fh = entrada[2]
    fm = entrada[3]
    h = 0
    m = 0
    if im - fm > 0:
        m = 60 - (im - fm)
        h-=1
    elif im - fm < 0:
        m = fm - im

    if fh - ih > 0:
        h += fh - ih
    else:
        h += 24 - abs(fh - ih)
    if h == 24 and m >0 :
        h = 0
    print(f'O JOGO DUROU {h} HORA (S) E {m} MINUTOS (S)')

