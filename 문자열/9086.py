"""
문자열을 입력으로 주면 물자열의 첫글자와 마지막 글자를 출력하는 프로그램
"""

test_num = int(input())
for i in range(test_num):
    word = list(input())
    print(f'{word[0]}{word[len(word)-1]}')