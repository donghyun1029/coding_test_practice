"""
최댓값과 위치 구하기
"""
max = 0
cnt_row = 0
cnt_col = 0

for i in range(9):
    A = list(map(int, input().split()))
    for j in range(9):
        if A[j] >= max:
            max = A[j]
            cnt_col = j+1
            cnt_row = i+1
        else:
            continue

print(max)
print(cnt_row, cnt_col)
