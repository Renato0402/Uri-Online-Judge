
if __name__ == '__main__':
    while True:

        try:
            count = int(input().strip())
            v = list(map(int, input().strip().split()))
            i = 0
            j = len(v)-1
            s1 = 0
            s2 = 0

            while i<=j:
                if s1 + v[i] <= s2 + v[j]:
                    s1+=v[i]
                    i+=1
                else:
                    s2+=v[j]
                    j-=1

            print(abs(s1-s2))

        except EOFError:
            break