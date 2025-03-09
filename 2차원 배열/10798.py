"""
세로읽기
"""

row = 5
array = [[] for i in range(row)]
A = []
count = 0

for i in range(row):
    A = list(input())
    for j in range(len(A)):
        array[i].append(A[j])
        count += 1

print(array)
print(count)

# array 받기까지는 완료
# 뒤집어서 출력 하는 코드 작성하면 됨
