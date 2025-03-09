"""
그룹 단어 체커

문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
"""
# hello -> h, e, ll, o 4개
# abab - > a, b, a, b 4개 ----> set 과 갯수가 다름
# year -> y, e, a, r 4개

"""word = list(input())
alpha = list(set(input()))
num_alpha = len(alpha)  """    #set 갯수

"""# 연속되는 같은 알파벳 묶어서 갯수 세기
def num_group_alpha(str):
    count = 1                  #
    for i in range(len(str) - 1):
        if str[i] == str[i+1]:
            continue
        else:
            count += 1
    return count

# set 과 num_group의 갯수가 같은지 확인
def check_group(str):
    before_sort = num_group_alpha(str)
    after_sort = num_group_alpha(sorted(str))
    if before_sort == after_sort:
        return True
    else:
        return False

num_group_word = 0
for i in range(int(input())):
    if check_group(input()):
        num_group_word += 1

print(num_group_word)"""
"""print(word)
print(alpha)"""

result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1

print(result)