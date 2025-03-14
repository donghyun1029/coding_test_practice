"""
output1:
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
"""

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
    print(f'Case #{j+1}: {list1[j]} + {list2[j]} = {listT[j]}')