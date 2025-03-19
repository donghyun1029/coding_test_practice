"""
나는야 포켓몬 마스터 이다솜
https://www.acmicpc.net/problem/1620
"""
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
name_dic = {}
name_list = []
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    name_list.append(name)

for index, name in enumerate(name_list, start = 1):
    name_dic[index] = name
reverse_name_dic = {v: k for k,  v in name_dic.items()}

question_list = []
for _ in range(M):
    question_list.append(sys.stdin.readline().rstrip())

for i in question_list:
    if i.isdigit() and int(i) in name_dic:
        print(name_dic[int(i)])
    elif i in reverse_name_dic:
        print(reverse_name_dic[i])
    else:
        continue