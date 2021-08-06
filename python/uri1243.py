import re

if __name__ == '__main__':

    while True:
        try:
            entrada = input().split()
            soma = 0
            qtd = 0

            for i in entrada:

                if bool(re.search(r'^[a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]+\.?$',i)):

                    soma += len(i)
                    qtd += 1

                    if i[len(i)-1] == '.':
                       soma-=1

            if qtd != 0:
                soma = int(soma / qtd)

            if soma <= 3:
                print(250)

            if soma == 4 or soma == 5:
                print(500)

            if soma >= 6:
                print(1000)




        except EOFError:
            break
