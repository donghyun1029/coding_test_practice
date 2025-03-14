"""
별찍기 (오른쪽 정렬)
"""

n = int(input())
for i in range(n):
    print(f'{(n - (i+1))*" "}{"*" * (i+1)}')
