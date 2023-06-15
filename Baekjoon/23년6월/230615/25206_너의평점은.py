import sys

lst = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
       'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
result = 0.0
c_sum = 0.0
for _ in range(20):
    sub, credit, score = sys.stdin.readline().split()
    # 등급이 P가 아닌경우 학점 * 과목평점 result에, 학점은 c_sum에 더해주기
    if score != 'P':
        result += float(credit) * lst[score]
        c_sum += float(credit)
# result를 c_sum으로 나눠서 출력
print(round(result/c_sum, 6))
