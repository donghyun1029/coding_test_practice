import sys
n = int(sys.stdin.readline())
list1 = []
list2 = []
listT = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    list1.append(a)
    list2.append(b)

for j in range(n):
    listT.append(list1[j] + list2[j])
    print(listT[j])
