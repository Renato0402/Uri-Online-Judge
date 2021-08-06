if __name__ == '__main__':
        s1 = input()
        s2 = input()
        s3 = input()
        s5 = ''

        ss1 = [s1,s2,s3]
        ss2 = [s2,s3,s1]
        ss3 = [s3,s1,s2]
        ss4 = [s1,s2,s3]
        for s in ss1:
            print(s,end='')
        print('')
        for s in ss2:
            print(s,end='')
        print('')
        for s in ss3:
            print(s,end='')

        print('')

        for x in range(len(s1)):
            s5+=s1[x]
            if x == 9:
                break
        for x in range(len(s2)):
            s5+=s2[x]
            if x == 9:
                break
        for x in range(len(s3)):
            s5+=s3[x]
            if x == 9:
                break

        print(s5)