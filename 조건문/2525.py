"""
오븐 완료 시간 출력
input: 
14 30
20

output:
14 50
"""
# b+c 1) 60 미만, 2) 60 이상 -> 시 = a+(b+c)//60, 분 = (b+c)%60
# a+((b+c)//60) 1) 24 미만, 2) 24 이상 -> -24

a, b = map(int, input().split())
c = int(input())

min = b+c
hour = a

if min < 60:
    print(hour, min)
else:
    hour = hour + (min//60)
    min = min % 60
    if hour < 24:
        print(hour, min)
    else:
        print(hour-24, min)