if __name__ == '__main__':
    count = int(input())
    for i in range(0,count):
        n = input().split()
        print(len(str(pow(int(n[0]),int(n[1])))))