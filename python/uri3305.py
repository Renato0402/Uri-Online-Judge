

count = int(input())
c = 0
first = True
v = []
max = 100000

for i in range(max+1):
        v.append([False,0])

for i in range(count):
        n = list(map(int, input().split()))
        if not v[abs(n[0] - n[1])][0]:
            v[abs(n[0] - n[1])][0] = True

        if v[abs(n[0] - n[1])][0]:
            v[abs(n[0] - n[1])][1]+=1

for i in v:

        if i[1]==1:
            c+=1

print(c)
