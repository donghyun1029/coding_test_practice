"""
색종이

문제
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 
이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 색종이의 수가 주어진다. 
이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 
색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다

출력
첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.

"""
# 100 x 100 matrix -> one 0 is same as 1 in terms of area
white_board = [[0 for j in range(100)] for i in range(100)]

N = int(input())
for i in range(N):
    a, b = map(int, input().split())    #left bottom corner coordinate
    
    for j in range(10):                 # replace 0 to 1 where black is covering
        for k in range(10):
            white_board[a+j][b+k] = 1

# count 1s
cnt = 0
for i in range(100):
    for j in range(100):
        if white_board[i][j] == 1:
            cnt += 1
        else:
            pass

print(cnt)