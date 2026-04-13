"""
제2장: 변수, 연산자, 문자열
으뜸 파이썬 Express — 예제 코드
"""

# ============================================================
# 출력 함수 print()와 주석
# ============================================================

print('Hello Python!!')

print('My age is', 20)
print('Steps today', 8000, 'steps')

# --- print() 함수의 end와 sep 인자 ---
# end parameter: use a space instead of newline after output
print('Hello', end=' ')
print('Python!')

# sep parameter: change separator between values to '-'
print('2025', '04', '07', sep='-')

# using sep and end together
print('A', 'B', 'C', sep=', ', end='!\n')

print('Hello ' * 2)
print('Hello ' * 4)
print('=' * 30)

# This line is a comment (not executed)
print('Hello')  # Inline comment: only the part after # is a comment

# ============================================================
# 변수와 자료형
# ============================================================

# --- 변수 없이 원의 정보를 출력하는 프로그램 \{ ---
print('Radius of circle', 4.0)
print('Area of circle', 3.14 * 4.0 * 4.0)
print('Circumference of circle', 2.0 * 3.14 * 4.0)

# --- 변수를 이용하여 원의 정보를 출력하는 프로그램 \{ ---
radius = 4.0
print('Radius of circle', radius)
print('Area of circle', 3.14 * radius * radius)
print('Circumference of circle', 2.0 * 3.14 * radius)

name = 'Hong Gildong'
print('Name :', name)
width = 10
height = 5
rectangle_area = width * height
print('Area of rectangle :', rectangle_area)

age = 27
print(age)
age = 23
print(age)

x = 10
type(x)
y = 3.14
type(y)
name = 'Hong Gildong'
type(name)
flag = True
type(flag)

int(3.7)
float(10)
str(100)
int('25')

age = input('Enter your age: ')
type(age)
age = int(age)
type(age)

# ============================================================
# 연산자
# ============================================================

10 + 3
10 / 3
10 // 3
10 % 3
2 ** 10

2 + 3 * 4
(2 + 3) * 4
2 ** 3 ** 2

(5 > 3) and (10 > 7)
(5 > 3) or (10 < 7)
not (5 > 3)

x = 10
x += 5
print(x)
x -= 3
print(x)
x *= 2
print(x)
x //= 5
print(x)

sum = 100
lst = [10, 20, 30]
total = sum(lst)

# ============================================================
# 문자열 다루기
# ============================================================

s1 = 'Hello'
s2 = "Python"
s3 = "'You can write
multi-line
strings."'
print(s3)

s = 'Python'
s[0]
s[3]
s[-1]
s[-2]

s = 'Python'
s[0:3]
s[2:5]
s[:3]
s[3:]
s[:]

s = 'Python'
s[0:6:2]
s[::-1]

'Hello' + ' ' + 'Python'
'Ha' * 3
len('Python')

s = 'Hello Python'
s.upper()
s.lower()
s.find('Python')
s.replace('Python', 'World')
'a,b,c'.split(',')

# --- 문자열 포매팅 ---
name = 'Hong Gildong'
age = 27

# format() method
print('Name: {}, Age: {}'.format(name, age))

# f-string (Python 3.6+)
print(f'Name: {name}, Age: {age}')

# expressions are also possible in f-strings
radius = 5.0
print(f'Area of circle: {3.14 * radius ** 2}')

x = 10          # x is int
x = 'hello'     # now x is str (no error)

// C language example
int x = 10;        /* x is declared as int */
x = "hello";       /* compile error! type mismatch */
