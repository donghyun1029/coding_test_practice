"""
세 자리 수 x 세 자리 수
input: 
472
385

output:
2360
3776
1416
181720
"""
a = input()
b = input()

c = int(a) * (int(b) - (int(b)//10) * 10)
d = int(a) * ((int(b) - (int(b)//100)*100 - (int(b) - (int(b)//10) * 10))//10)
e = int(a) * (int(b)//100)

print(c)
print(d)
print(e)
print(c + (10*d) + (100*e))