if __name__ == '__main__':
    n1 = list(map(int,input().split()))
    n2 = list(map(int, input().split()))
    n3 = list(map(int, input().split()))
    n4 = list(map(int, input().split()))

    maior = max(sum(n1),sum(n2),sum(n3),sum(n4))
    m2 = maior

    v = []
    while maior >= 1:
        v.append(str(maior % 2))
        maior = int(maior/2)

    print(m2,'=',''.join(v)[::-1])