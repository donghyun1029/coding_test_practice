"""
수 정렬하기 3

문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""
# 이 문제는 모든 입력을 배열이나 리스트에 저장해놓고 푸는 것이 의도된 문제가 아닙니다. 
# 문제의 상단을 잘 보시면 메모리 제한은 겨우 8 MB이고 N은 최대 1000만인 것을 확인할 수 있습니다.
# N개의 독립된 원소를 어딘가에 전부 들고 있으면 메모리 초과로 곧바로 이어질 가능성이 높습니다. 
# 그렇기 때문에 일반적으로 정렬에 사용하는 merge sort, heap sort, quick sort 등이나 내장 정렬 함수 등도 전부 사용을 할 수 없습니다.

# 핵심은 입력으로 주어지는 수들이 전부 1만 이하라는 것입니다. 
# 이를 어떻게 이용하면 이런 빠듯한 제한 내에서도 모든 수에 대한 정보를 저장하고 정렬된 상태로 출력까지 할 수 있을지 생각해 보세요. 
# 모든 수를 개별적으로 저장하지 않아도 그에 대한 정보만 표현할 수 있으면 되고, 정렬을 실제로 하지 않아도 정렬된 상태로 출력만 할 수 있으면 된다는 것이 중요합니다. 

import sys

N = int(sys.stdin.readline().rstrip())
cnt_dic = {}

#디셔너리에 저장하기
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    # num 이 딕셔너리에 없으면 기본값 0부터 +1 하여 카운트 추가
    cnt_dic[num] = cnt_dic.get(num, 0) + 1

# 딕셔너리 안 키 정렬
for key in sorted(cnt_dic.keys()):
    # 키의 value 갯수만큼 키 출력
    for _ in range(cnt_dic[key]):
        print(key)