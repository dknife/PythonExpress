# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.5: if-else 문을 이용한 오전/오후 판별  —  if_else_hour_test.py

hour = int(input('Enter the hour: '))
if hour < 12:
    print('It is AM.')
else:
    print('It is PM.')
