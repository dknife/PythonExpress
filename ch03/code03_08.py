# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.8: 논리 연산자를 활용한 복합 조건식  —  if_modulo2.py

number = int(input('Enter an integer: '))
if number % 3 == 0 and number % 5 == 0:
    print(number, 'is a multiple of both 3 and 5.')
elif number % 3 == 0:
    print(number, 'is a multiple of 3.')
elif number % 5 == 0:
    print(number, 'is a multiple of 5.')
else:
    print(number, 'is neither a multiple of 3 nor 5.')
