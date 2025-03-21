"""
좌표 정렬하기

문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
"""

import sys

N = int(sys.stdin.readline())
coor_dic = {}

# 한개의 딕셔너리 key(x) 에 여러개 value(y) 값 저장
for _ in range(N):
    key, value = map(int, sys.stdin.readline().split())
    if key not in coor_dic:
        #coor_dic[key] = coor_dic.get(key, value)
        coor_dic[key] = [value]
    else:
        coor_dic[key].append(value)

# 오름차순 정렬 후 출력
for key in sorted(coor_dic.keys()):
    for value in sorted(coor_dic[key]):
        print(key, value)