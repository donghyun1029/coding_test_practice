"""
체스판 다시 칠하기

문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.
"""
# x + y 가 2의 짝수이면 W, 홀수면 B

M, N= map(int, input().split())
board = []
temp1 =[]

# replaced W&B to number 1&0
for i in range(M):
    temp1 = list(input())
    #print("temp1", temp1)
    temp2 = []
    for j in temp1:
        if j == "B":    # B = 0
            j1 = j.replace("B", "0")
        else:           # W = 0
            j1 = j.replace("W", "1")
        temp2.append(int(j1))
    board.append(temp2)

min_count = 64

for i in range(M - 7):
    for j in range(N-7):
        count1 = 0
        count2 = 0
        count = 0
        for x in range(8):
            for y in range(8):
                #if board[i][j] == 0:    # B
                if (x+y)%2 == 0:    # B
                    if board[x+i][y+j] != 0:
                        count1 += 1
                else:               # W
                    if board[x+i][y+j] != 1:
                        count1 += 1
                #else:                   # W
                if (x+y)%2 == 0:    # W
                    if board[x+i][y+j] != 1:
                        count2 += 1
                else:               # B
                    if board[x+i][y+j] != 0:
                        count2 += 1
        if count1 <= count2:
            count = count1
        else:
            count = count2

        #print("count", count)
        if count < min_count:
            min_count = count
            #print("min", min_count)
print(min_count)

        

"""min_change = 64
color_figure = 0
for i in board:
    temp = i.replace('B', 0)
    result
board.replace('B', 0)
board.replace('W', 1)"""
"""
for i in range(N - 7):
    for j in range(M-7):
        
        color_change = 0
        for x in range(8):
            for y in range(8):
                if board[i][j] == 'W':
                    if (((x+y)%2 == 0) and (board[i+x][j+y] == 'B')) or (((x+y)%2 == 1) and (board[i+x][j+y] == 'W')):
                        color_change += 1
                else:
                    if (((x+y)%2 == 0) and (board[i+x][j+y] == 'W')) or (((x+y)%2 == 1) and (board[i+x][j+y] == 'B')):
                        color_change += 1
        
        if color_change < min_change:
            min_change = color_change
            print(min_change)
        
print(min_change)
"""
