# 피보나치 함수 만들기
def fibonacci(num):
    # 숫자가 이전 배열의 길이보다 크면 zero와 one에 값 추가해주기
    if num >= len(zero):
        for i in range(len(zero), num+1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[num], one[num])


# 0, 1, 2일 때 0과 1이 출력되는 횟수 배열에 저장
zero = [1, 0, 1]
one = [0, 1, 1]

T = int(input()) 
for _ in range(T):
    fibonacci(int(input()))