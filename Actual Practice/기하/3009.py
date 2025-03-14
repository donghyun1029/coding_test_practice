"""
네 번째 점

문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.

*P3(x1, y1+b)           *P4(x1+a, y1+b)

*P1(x1, y1)             *P2(x1+a, y1)

"""
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

while True:
    # 첫 입력 받을 것을 기준 (p1)
    if x1 == x2:
        if y1 == y3:
            print(x3, y2)
            break
        else:
            print(x3, y1)
            break
    # 30 20
    # 10 10
    # 10 20
    elif x2 == x3: # print(x1, )
        if y1 == y2: 
            print(x1, y3)
            break
        else: #y1 == y3
            print(x1, y2)
            break

    # 30 20
    # 10 20
    # 30 10
    else: # x1 == x3 (print(x2, ))
        if y1 == y2:
            print(x2, y3)
            break
        else:
            print(x2, y1)
            break