"""
입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

입력의 마지막에는 0 두 개가 들어온다.

input:
1 1
2 3
3 4
9 8
5 2
0 0

output:
2
5
7
17
7
"""
listT = []
i = 0
stop = 0

while True:
    a, b = map(int, input().split())
    listT.append(a+b)
    if (a + b) == 0:
        break
    i += 1
    
for j in range(i):
    print(listT[j])
