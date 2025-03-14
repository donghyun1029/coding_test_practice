"""
소수 찾기

문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
"""

N = int(input())
cnt = 0
a = []

a = list(map(int, input().split()))
print("a", a)

for i in range(len(a)):
    common = []
    for j in range(a[i]):
        if a[i] % (j+1) == 0:
            common.append(j+1)
            print(common)

    if len(common) == 2:
        cnt += 1

print(cnt)