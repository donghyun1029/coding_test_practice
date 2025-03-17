"""
수학은 비대면 강의 입니다

https://www.acmicpc.net/problem/19532

ax + by = c =>  x = -b/a y + c/a
dx + ey = f =>  x = -e/d y+ f/d
                -b/a y + c/a = -e/d y+ f/d
                (e/d - b/a)y = f/d - c/a
                y = (f/d - c/a) / (e/d - b/a)
                x = -(b/a)((f/d - c/a) / (e/d - b/a)) + c/a

-999 <= a, b, c, d, e, f <= 999
"""

a, b, c, d, e, f = map(int, input().split())

x = (c * e - b * f) / (a * e - b * d)
y = (c * d - a * f) / (b * d - a * e)

print(int(x), int(y))

