"""
제3장: 조건문과 반복문
으뜸 파이썬 Express — 예제 코드
"""

# ============================================================
# 순차문과 제어문
# ============================================================

# --- 순차적 실행 구조를 이용한 변수의 덧셈 \{ ---
num = 100
print('num =', num)
num = num + 100
print('num =', num)
num = num + 100
print('num =', num)

# ============================================================
# if 조건문
# ============================================================

# --- if 조건문을 이용한 출력 \{ ---
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

# --- if-else 문을 이용한 오전/오후 판별 \{ ---
hour = int(input('Enter the hour: '))
if hour < 12:
    print('It is AM.')
else:
    print('It is PM.')

# --- if-else 문을 이용한 짝수/홀수 판별 \{ ---
num = int(input('Enter a positive integer: '))
if num % 2 == 0:
    print(num, 'is even.')
else:
    print(num, 'is odd.')

# --- if-elif-else 조건문으로 학점 판정 \{ ---
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

# --- 논리 연산자를 활용한 복합 조건식 \{ ---
number = int(input('Enter an integer: '))
if number % 3 == 0 and number % 5 == 0:
    print(number, 'is a multiple of both 3 and 5.')
elif number % 3 == 0:
    print(number, 'is a multiple of 3.')
elif number % 5 == 0:
    print(number, 'is a multiple of 5.')
else:
    print(number, 'is neither a multiple of 3 nor 5.')

# --- 중첩 조건문 \{ ---
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

# --- for 문을 이용한 반복 출력 \{ ---
for i in range(5):
    print('Welcome to everyone!!')

list(range(5))
list(range(1, 6))
list(range(0, 10, 2))
list(range(10, 0, -1))
list(range(-2, -10, -2))

# --- 1부터 10까지의 합 구하기 \{ ---
s = 0
for i in range(1, 11):
    s = s + i
print('Sum from 1 to 10:', s)

# --- for 반복문을 이용한 팩토리얼 계산 \{ ---
n = int(input('Enter a number: '))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(f'{n}! = {fact}')

# --- 리스트와 문자열 순회 ---
# iterating over a list
fruits = ['apple', 'banana', 'grape']
for fruit in fruits:
    print(fruit, end=' ')
print()

# iterating over a string
for ch in 'Python':
    print(ch, end=' ')
print()

# --- 이중 for 문으로 구구단 전체 출력 \{ ---
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i}*{j}={i*j:2d}', end='  ')
    print()

# ============================================================
# while 반복문과 흐름 제어
# ============================================================

# --- while 문의 기본 사용 \{ ---
i = 1
while i <= 5:
    print(i, end=' ')
    i += 1
print()

# --- 사용자 입력을 이용한 while 문 \{ ---
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

# --- break 문으로 반복 중단 \{ ---
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=' ')
print()
print('Loop ended')

# --- continue 문으로 홀수만 출력 \{ ---
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print()

# --- 반복문과 조건문을 조합한 짝수/홀수 합 \{ ---
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

nums = [1, 3, 5, 7, 9]
target = 4
for n in nums:
    if n == target:
        print(f'Found {target}!')
        break
else:
    print(f'{target} is not in the list.')
