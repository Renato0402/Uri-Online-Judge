import re

if __name__ == '__main__':
    while True:
        try:
            n = input()
            str = ''
            str2 = ''
            t = False

            for i in range(len(n)):

                if n[i] == 'o' or n[i] == 'O':
                    str += '0'
                elif n[i] == 'l':
                    str += '1'
                else:
                    str += n[i]

            if n == '' or bool(re.search(r'^[\s]+$', n)) or bool(re.search(r'[a-zA-Z]+\s?[0-9]+', str))\
                    or bool(re.search(r'^[a-zA-Z]+$', str)) or bool(re.search(r'[0-9]+\s?[a-zA-Z]+', str))\
                    or str.__contains__('.') or str.__contains__('-') or (str.startswith(',') and len(str)==1)\
                    :
                print('error')
                t = True



            regex = re.findall(r'\d', str)
            for x in regex:
                str2 += x

            if bool(re.search(r'^[0-9]+$', str2)):
                if int(str2) > 2147483647:
                    print('error')

            if bool(re.search(r'^[0-9]+$', str2)):
                if 2147483647 >= int(str2) > 0 and not t:
                    print(str2.lstrip('0'))

            if bool(re.search(r'^[0]+$', str2)):
                print('0')

        except EOFError:
            break
