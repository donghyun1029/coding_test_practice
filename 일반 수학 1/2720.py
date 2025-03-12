"""
거스름돈

quater: 0.25 -> 25
dime: 0.1 -> 10
Nickel: 0.05 -> 5
penny: 0.01 -> 1
"""
coin = [25, 10, 5, 1]

q = 0
r = 0

for i in range(int(input())):
    change = int(input())
    total_change = []
    for j in coin:    
        q = change // j
        r = change % j
        total_change.append(q)
        change = r
    print(' '.join(map(str, total_change)))