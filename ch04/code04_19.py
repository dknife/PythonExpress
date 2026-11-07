# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.19: 사용자 입력을 받는 사칙연산 함수

def calc(a, b):
    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {a / b:.2f}')

x = int(input('첫 번째 수를 입력하세요: '))
y = int(input('두 번째 수를 입력하세요: '))
calc(x, y)
