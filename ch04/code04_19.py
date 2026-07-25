# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.19: 사용자 입력을 받는 사칙연산 함수

def calc(a, b):
    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {a / b:.2f}')

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
calc(x, y)
