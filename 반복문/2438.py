"""
별 찍기
input: 5
output:
*
**
***
****
*****
"""

n = int(input())
for i in range(n):
    print('*' * (i+1))