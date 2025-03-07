"""
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
"""

n = int(input())
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print(sum)