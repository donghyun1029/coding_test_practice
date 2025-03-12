"""
세로읽기
"""

row = 5
array = [["*" for j in range(15)] for i in range(row)]  # 5x15 matrix
A = []

for i in range(row):
    A = list(input())           # 1x5 matrix 를 array 에 삽입
    print(A)
    for j in range(len(A)):
        array[i][j] = A[j]

print(array)

# * 이 아닌 문자를 ans 배열에 원하는 순서대로 삽입. ans 는 1차원 배열
ans = []
for i in range(len(array[i])):
    for j in range(len(array)):
        if array[j][i] != '*':
            ans.append(array[j][i])

print(''.join(map(str, ans)))


"""
result_list = []
for i in range(len(array)):
    for j in range(len(array[i])):
        temp = array[i][j].replace("*", "")
        result_list.append(temp)

print(result_list)"""

# array 받기까지는 완료 -> 애초에 뒤집어서 받자 [i][j] ->[j][i]
# 뒤집어서 출력 하는 코드 작성하면 됨
"""
for i in range(len(array[i])):
    for j in range(len(array)):
        if len(array[i]) :
            pass
        else:
            print(array[j][i])

    for j in range():
        if array[i][j] == False:
            pass"""