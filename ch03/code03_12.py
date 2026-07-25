# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.12: for 반복문을 이용한 팩토리얼 계산  —  for_factorial.py

n = int(input('Enter a number: '))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(f'{n}! = {fact}')
