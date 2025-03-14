"""
벌집

1   1                   1~1     1 + 6*0                 1 + 6*0
2   6   2*6 - 6 = 6     2~7     1 + 6*1                 1 + 6*1
3   12  3*6 - 6 = 12    8~19    1 + 6*1 + 6*2           1 + 6*3
4   18  4*6 - 6 = 18    20~37   1 + 6*1 + 6*2 + 6*3     1 + 6*6

1000000 //6
"""
a = 0
b = 1
layer = []
door = []
max_num_layer = []

N = int(input())

while True:
#    layer.append(a)
    door.append(b)
    max_num_layer.append(1+6*a)
    a += b
    b += 1
    if 1+6*a > 1000000000:
        break

#print(layer, door, max_num_layer)

for i in range(len(max_num_layer)):
    if N == 1:
        print(1)
        break
    if (N > max_num_layer[i]) and (N <= max_num_layer[i+1]):
        print(door[i+1])
        break
"""    else:
        print("break")
        break"""
