"""
제3장: 조건문과 반복문
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 순차문과 제어문
# ============================================================

num = 100
print('num =', num)
num = num + 100
print('num =', num)
num = num + 100
print('num =', num)

# ============================================================
# if 조건문
# ============================================================

age = 18
if age < 20:
    print('Youth discount')

# --- 들여쓰기에 따른 블록의 범위 차이 (조건 만족 시) ---
age = 18
if age < 20:
    print('Youth discount')
print('Welcome!')

# --- 세 개의 print 문이 모두 블록 안에 있는 경우 ---
age = 18
if age < 20:
    print('Age:', age)
    print('Youth discount')
    print('Welcome, young person!')

hour = int(input('Enter the hour: '))
if hour < 12:
    print('It is AM.')
else:
    print('It is PM.')

# --- if-else 문을 이용한 짝수/홀수 판별 — if_else_even_test.py ---
num = int(input('Enter a positive integer: '))
if num % 2 == 0:
 print(num, 'is even.')
else:
 print(num, 'is odd.')

score = int(input('Enter score: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f'Grade: {grade}')

# --- 논리 연산자를 활용한 복합 조건식 — if_modulo2.py ---
number = int(input('Enter an integer: '))
if number % 3 == 0 and number % 5 == 0:
 print(number, 'is a multiple of both 3 and 5.')
elif number % 3 == 0:
 print(number, 'is a multiple of 3.')
elif number % 5 == 0:
 print(number, 'is a multiple of 5.')
else:
 print(number, 'is neither a multiple of 3 nor 5.')

# --- 중첩 조건문 — nested_if.py ---
age = int(input('Enter your age: '))
if age >= 20:
 if age >= 65:
 print('Senior discount')
 else:
 print('Regular adult')
else:
 print('Minor')

# ============================================================
# for 반복문
# ============================================================

for i in range(5):
    print('Welcome to everyone!!')

list(range(5))
list(range(1, 6))
list(range(0, 10, 2))
list(range(10, 0, -1))
list(range(-2, -10, -2))

s = 0
for i in range(1, 11):
    s = s + i
print('Sum from 1 to 10:', s)

n = int(input('Enter a number: '))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(f'{n}! = {fact}')

# 리스트 순회
fruits = ['apple', 'banana', 'grape']
for fruit in fruits:
    print(fruit, end=' ')
print()

# 문자열 순회
for ch in 'Python':
    print(ch, end=' ')
print()

# --- 이중 for 문으로 구구단 전체 출력 — double_for.py ---
for i in range(2, 10):
 for j in range(1, 10):
 print(f'{i}*{j}={i*j:2d}', end=' ')
 print()

# ============================================================
# while 반복문과 흐름 제어
# ============================================================

i = 1
while i <= 5:
    print(i, end=' ')
    i += 1
print()

# --- 사용자 입력을 이용한 while 문 — while_input.py ---
total = 0
count = 0
num = int(input('Enter a number (0 to quit): '))
while num != 0:
 total += num
 count += 1
 num = int(input('Enter a number (0 to quit): '))
if count > 0:
 print(f'Sum: {total}, Average: {total/count:.1f}')
else:
 print('No numbers were entered.')

for i in range(1, 11):
    if i == 6:
        break
    print(i, end=' ')
print()
print('Loop ended')

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print()

even_sum = 0
odd_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f'Sum of even numbers: {even_sum}')
print(f'Sum of odd numbers: {odd_sum}')

# --- while True와 break를 이용한 입력 처리 ---
while True:
    text = input('Enter text (quit to exit): ')
    if text == 'quit':
        print('Goodbye!')
        break
    print(f'You entered: {text}')

# --- 1부터 5까지 출력하는 for 문 ---
for i in range(1, 6):
    print(i, end=' ')
print()

# --- 같은 동작을 while 문으로 옮긴 코드 ---
i = 1 # 초기값 설정
while i < 6: # 조건 검사
    print(i, end=' ')
    i += 1 # 갱신
print()

# ============================================================
# 실습을 통한 3장 개념 정리
# ============================================================

game_score = int(input('Enter game score: '))
if game_score >= 1000:
    print('고수입니다')
else:
    print('입문자입니다')

n = int(input('Enter an integer: '))
if n % 2 == 0:
    print('짝수입니다')
else:
    print('홀수입니다')

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)

n = int(input('Enter n: '))
total = 0
for i in range(1, n + 1):
    total += i
print(total)

n = int(input('Enter n: '))
f = 1
for i in range(1, n + 1):
    f *= i
print(f)

while True:
    s = input('Enter text: ')
    if s == 'quit':
        break
    print(s)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')
print()

n = int(input('Enter n: '))
total = 0
i = 1                       # 초기값 설정
while i <= n:               # 조건 검사
    total += i
    i += 1                  # 갱신
print(total)
