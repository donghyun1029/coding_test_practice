"""
직사각형에서 탈출

문제
한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 x, y, w, h가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다.
"""

x, y, w, h = map(int, input().split())

boarder_x = [0, w]
boarder_y = [0, h]
dis_x = []
dis_y = []
for i in range(2):
    dis_x.append(abs(x - boarder_x[i]))
    dis_y.append(abs(y - boarder_y[i]))

print(dis_x, dis_y)

if min(dis_x) >= min(dis_y):
    print(min(dis_y))
else:
    print(min(dis_x))

#print(min(dis))