import math

if __name__ == '__main__':
    count = int(input())

    for x in range(count):

        s = input()
        half = math.floor(len(s) / 2)
        str = ''
        aux = half

        while aux != half + 1:

            str += s[aux - 1]

            if aux == 1:
                aux = len(s)
                str += s[aux - 1]

            aux -= 1

        str += s[half]
        print(str)
