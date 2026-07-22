"""
제4장: 함수와 입출력
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 함수의 역할과 정의
# ============================================================

# --- 함수 정의의 기본 문법 ---
def function_name(param1, param2,...):
 code to execute
 return value # 생략 가능

def print_star(): # 별표를 출력하는 함수 정의
 print('************************')

print_star() # 함수 호출 1
print_star() # 함수 호출 2
print_star() # 함수 호출 3

def print_star():
 print('************************')

def print_plus():
 print('++++++++++++++++++++++++')

print_star()
print_plus()
print_star()
print_plus()

# ============================================================
# 매개변수와 반환값
# ============================================================

def print_star(n): # n은 매개변수
 for _ in range(n):
 print('************************')

print_star(4) # 4는 인자

def print_sum(a, b):
 result = a + b
 print('The sum of', a, 'and', b, 'is', result)

print_sum(10, 20)
print_sum(100, 200)

def greet(name, greeting='Hello'):
 print(f'{greeting}, {name}!')

greet('Alice') # 기본값 사용
greet('Bob', 'Nice to meet you') # 기본값 대신 전달한 값 사용

greet(greeting='Welcome', name='Charlie')

def average(*scores): # 모든 위치 인자를 튜플로 받음
 if len(scores) == 0:
 return 0
 return sum(scores) / len(scores)

print(average(80, 90, 100)) # 인자 3개
print(average(70, 85, 95, 100)) # 인자 4개

def make_profile(**info): # 키워드 인자를 딕셔너리로 받음
 for key, value in info.items():
 print(f'{key}: {value}')

make_profile(name='Alice', age=20, job='Designer')

def get_sum(a, b):
 return a + b

result = get_sum(100, 200)
print('Sum of two numbers:', result)

def get_root(a, b, c):
 r1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
 r2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
 return r1, r2 # 두 값을 반환

result1, result2 = get_root(1, 2, -8)
print('The roots are', result1, 'or', result2)

def add(a: int, b: int) -> int:
 return a + b

def greet(name: str, times: int = 1) -> None:
 for _ in range(times):
 print(f'Hello, {name}!')

def factorial(n):
 if n <= 1: # 기저 조건
 return 1
 return n * factorial(n - 1) # 재귀 단계

print(factorial(5)) # 120
print(factorial(7)) # 5040

def gcd(a, b):
 if b == 0: # 기저 조건
 return a
 return gcd(b, a % b) # 재귀 단계

print(gcd(48, 18)) # 6
print(gcd(100, 75)) # 25

# ============================================================
# 변수의 범위
# ============================================================

x1 = 10
x2 = 20
x3 = 30

def my_function() :
 global x1

 x1 = 1 # 전역변수 x1 (global로 선언됨)
 x2 = 2 # 지역변수 x2 (할당으로 생성)
 y1 = 40 # 지역변수
 y2 = 50

 print('inside function: ', x1, x2, x3, y1, y2)


my_function(); # 함수 호출, x1, x2, x3, y1, y2 출력
 # 예상 출력: 1, 2, 30, 40, 50

print('outside function -')
print(x1, x2, x3) # 전역변수 x1, x2, x3
 # 예상 출력: 1, 20, 30

print(y1, y2) # 지역변수 y1, y2는 접근 불가
 # 예상 결과: NameError

x = 100 # 전역변수

def change_x():
 x = 999 # 지역변수 (전역변수와 별개)
 print('Inside function x:', x)

change_x()
print('Outside function x:', x) # 전역변수는 변하지 않음

count = 0 # 전역변수

def increment():
 global count # 전역변수 count 사용 선언
 count += 1

increment()
increment()
increment()
print('count =', count)

# ============================================================
# 입출력과 포매팅
# ============================================================

name = input('Enter your name: ')
print('Hello,', name, '!')

a = int(input('First integer: '))
b = int(input('Second integer: '))
print(f'{a} + {b} = {a + b}')

def calc(a, b):
 print(f'{a} + {b} = {a + b}')
 print(f'{a} - {b} = {a - b}')
 print(f'{a} * {b} = {a * b}')
 print(f'{a} / {b} = {a / b:.2f}')

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
calc(x, y)

print(abs(-7)) # 7
print(max(3, 7, 1)) # 7
print(min(3, 7, 1)) # 1
print(round(3.14159, 2)) # 3.14

n = int(input('How many numbers? '))
print('---- formatted ----')
for _ in range(n):
 x = float(input('Enter a number: '))
 print(f'{x:7.2f}') # 전체 폭 7자리, 소수점 2자리

n = int(input('How many numbers? '))
print('---- formatted ----')
for _ in range(n):
 x = float(input('Enter a number: '))
 print(f'{x:08.2f}') # 전체 폭 8자리, 빈 자리는 0으로 채움

# ============================================================
# 실습을 통한 4장 개념 정리
# ============================================================

def add(a, b):
    return a + b

print(add(3, 5))        # 8
print(add(100, 200))    # 300

def c_to_f(c):
    return c * 9 / 5 + 32

print(c_to_f(0))      # 32.0
print(c_to_f(100))    # 212.0
print(c_to_f(36.5))   # 97.7

def circle_area(r):
    return 3.14 * r * r

print(f'Area(r=5) : {circle_area(5)}')

def average(*nums):
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)

print(average(80, 90, 75))         # 81.666...
print(average(10, 20, 30, 40))     # 25.0
print(average())                   # 0

def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    return None

a  = float(input('First  number: '))
op = input('Operator (+, -, *, /): ')
b  = float(input('Second number: '))
print(f'{a} {op} {b} = {calculate(a, op, b)}')

def sum_and_factorial(n):
    s = 0
    f = 1
    for i in range(1, n + 1):
        s += i
        f *= i
    return s, f

total, fact = sum_and_factorial(5)
print(f'1+2+...+5 = {total}')   # 15
print(f'5! = {fact}')           # 120
