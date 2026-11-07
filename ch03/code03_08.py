# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.8: 논리 연산자를 활용한 복합 조건식

number = int(input('정수를 입력하세요: '))
if number % 3 == 0 and number % 5 == 0:
    print(number, ': 3과 5의 공배수입니다.')
elif number % 3 == 0:
    print(number, ': 3의 배수입니다.')
elif number % 5 == 0:
    print(number, ': 5의 배수입니다.')
else:
    print(number, ': 3의 배수도 5의 배수도 아닙니다.')
