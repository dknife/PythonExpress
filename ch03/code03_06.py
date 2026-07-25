# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.6: if-else 문을 이용한 짝수/홀수 판별  —  if_else_even_test.py

num = int(input('Enter a positive integer: '))
if num % 2 == 0:
    print(num, 'is even.')
else:
    print(num, 'is odd.')
