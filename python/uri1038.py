if __name__ == '__main__':
    entrada = input().split()
    code = int(entrada[0])
    qtd = int(entrada[1])
    v = [4.00,4.50,5.00,2.00,1.50]
    print('Total: R$ {:.2f}'.format(v[code-1]*qtd))