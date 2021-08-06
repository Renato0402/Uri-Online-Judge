if __name__ == '__main__':
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


    count = int(input())
    while count > 0:
     v = list(map(int, input().split()))
     quickSort(v, 0, len(v) - 1)
     cont = 0
     i = 0
     t = False
     while cont < 2 and i < len(v) - 1:
            t = True
            if v[i] == v[i + 1] and i < len(v) - 1:
                i += 2
            else:
                print(v[i],end=' ')

                cont+=1
                i+=1


     if cont != 2 and t:
        print(v[len(v)-1])




