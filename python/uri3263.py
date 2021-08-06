if __name__ == '__main__':
    count = int(input())
    s = input()
    s2 = input()
    s = list(s)
    for i in range(count):

     for j in range(len(s)):

        if s[j] == '1':
            s[j] = '0'
        else:
            s[j] = '1'

    s = ''.join(s)

    if s.__eq__(s2):
        print('Deletion succeeded')
    else:
        print('Deletion failed')

