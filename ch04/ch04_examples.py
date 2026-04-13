"""
제4장: 함수와 입출력
으뜸 파이썬 Express — 예제 코드
"""

# ============================================================
# 함수의 역할과 정의
# ============================================================

def function_name(param1, param2, ...):
    code to execute
    return value  # optional

def print_star():  # define a function that prints stars
    print('************************')

print_star()  # function call 1
print_star()  # function call 2
print_star()  # function call 3

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

def print_star(n):  # n is a parameter
    for _ in range(n):
        print('************************')

print_star(4)  # 4 is an argument

def print_sum(a, b):
    result = a + b
    print('The sum of', a, 'and', b, 'is', result)

print_sum(10, 20)
print_sum(100, 200)


def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')

greet('Alice')             # uses default value
greet('Bob', 'Nice to meet you')  # overrides default

greet(greeting='Welcome', name='Charlie')

def get_sum(a, b):
    return a + b

result = get_sum(100, 200)
print('Sum of two numbers:', result)

def get_root(a, b, c):
    r1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return r1, r2  # return two values

result1, result2 = get_root(1, 2, -8)
print('The roots are', result1, 'or', result2)

# ============================================================
# 변수의 범위
# ============================================================

x = 10  # global variable

def my_func():
    y = 20  # local variable
    print('Inside function: x =', x, ', y =', y)

my_func()
print('Outside function: x =', x)
# print(y)  # NameError: y is only available inside the function

x = 100  # global variable

def change_x():
    x = 999  # local variable (separate from global)
    print('Inside function x:', x)

change_x()
print('Outside function x:', x)  # global variable unchanged

count = 0  # global variable

def increment():
    global count  # declare use of global variable count
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

print('apple', 'banana', 'grape', sep=', ')
print('Hello', end=' ')
print('World')

name = 'Alice'
age = 20
print('Name: {}, Age: {}'.format(name, age))
print('Name: {0}, Age: {1}'.format(name, age))

name = 'Bob'
score = 95.678
print(f'{name}\'s score is {score:.1f} points.')
print(f'Pi: {3.14159:.2f}')
print(f'Integer formatting: {42:05d}')

print(abs(-7))           # 7
print(max(3, 7, 1))     # 7
print(min(3, 7, 1))     # 1
print(round(3.14159, 2)) # 3.14
