import math

if __name__ == '__main__':
    count = int(input())
    cc = 1


    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):

            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)


    def quickSort(arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(arr, low, high)
            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)

    while count != 0:

        cTotal = 0
        pTotal = 0
        v = []
        cont = 0
        arr = [0] * 200


        for i in range(count):
            n = input().split()
            p = int(n[0])
            c = int(n[1])

            cTotal += c
            pTotal += p
            arr[math.floor(c / p) - 1] += p
            v.append(math.floor(c / p))

        print(f'Cidade# {cc}:')
        quickSort(v,0,len(v)-1)


        for i in range(len(v)):
          if i!=len(v)-1:
              if v[i]!= v[i+1]:

               print(f'{arr[v[i] - 1]}-{v[i]}', end=' ')
          else:
            print(f'{arr[v[i] - 1]}-{v[i]}', end='')

        print('')
        n = cTotal / pTotal
        n = math.trunc(n*100)/100

        if not n.is_integer():
         print(f'Consumo medio: {n} m3.')

        else:
         print(f'Consumo medio: {n}0 m3.')


        count = int(input())
        cc += 1
