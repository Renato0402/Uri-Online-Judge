class pilha:
    v = []

    def push(self, element):
        self.v.append(element)

    def pop(self):
        self.v.pop(0)



if __name__ == '__main__':
    pilha = pilha()

    p = input().strip().split()

    for x in p:
        for j in x:
            if j == ')' and len(pilha.v) > 0:
                pilha.pop()
            if j == '(':
                pilha.push(j)

    if len(pilha.v)>0:
        print(f'Ainda temos {len(pilha.v)} assunto(s) pendente(s)!')
    else:
        print('Partiu RU!')
