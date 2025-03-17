"""
분해합

문제
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

"""

N = int(input())

min_sum = 0

"""if N == 1:
    print(0)
else:"""
for i in range(N):
    r = N - i
    #print("r", r)
    sum = r
    num_list = []
    while True:
        num_list.append(r%10)
        r = r//10
        if r == 0:
            break
    for j in num_list:
        sum += j

    #print("i", i)
    #print("sum", sum)
    if sum == N:
        min_sum = N - i

if min_sum == 0:
    print(0)
else:
    print(min_sum)

    """    
    if min_sum > sum and sum == N:
        min_sum == sum
    else:
        print(min_sum)"""

"""# 각자리수 나누는 함수
def slice_num(n):
    r = n
    num_list = []
    while True:
        num_list.append(r%10)
        r = r//10
        if r == 0:
            break
    return num_list
    
def find_sum(n, num_list):
    sum = n
    for i in num_list:
        sum += i
    return sum

temp = N
min_sum = 0
while True:
    temp_list = slice_num(temp)
    temp_sum = find_sum(temp, temp_list)
    if temp_sum == N:
        min_sum = temp_sum
        print(min_sum)
        print(temp, temp_list)
        print(temp_sum)
        temp -= 1
    else:
        temp -= 1
    
    if temp == 0:
        break"""


