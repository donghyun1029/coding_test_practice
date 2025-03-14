"""
너의 평점은

GPA 계산

input: 20개의 과목이름 + credit number + grade
output: Final GPA
"""
score = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}
import sys

cnt_credit = 0
total = 0

for i in range(20):
    class_name, credit, grade = sys.stdin.readline().split()
    if grade != 'P':
        #print(score[grade])
        weighted_grade = float(credit) * score[grade]
        #print(weighted_grade)
        total += weighted_grade
        cnt_credit += float(credit)
        #print(total, cnt_credit)
    else:
        continue

# final_grade = total / cnt_credit
print(total / cnt_credit)