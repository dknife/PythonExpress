"""
제2장: 변수, 연산자, 문자열
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 출력 함수 print()와 주석
# ============================================================

print('Hello Python!!')

print('My age is', 20)
print('Steps today', 8000, 'steps')

# end 인자: 출력 후 줄 바꿈 대신 공백 사용
print('Hello', end=' ')
print('Python!')

# sep 인자: 값 사이의 구분 문자를 '-'로 변경
print('2025', '04', '07', sep='-')

# sep과 end를 함께 사용
print('A', 'B', 'C', sep=', ', end='!\n')

print('Hello ' * 2)
print('Hello ' * 4)
print('=' * 30)

# --- 주석문 작성 예 ---
# 이 줄 전체가 주석 (실행되지 않음)
print('Hello') # 인라인 주석: # 뒤의 내용만 주석

# ============================================================
# 변수와 자료형
# ============================================================

print('Radius of circle', 4.0)
print('Area of circle', 3.14 * 4.0 * 4.0)
print('Circumference of circle', 2.0 * 3.14 * 4.0)

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

name = 'Hong Gildong'
age = 27

# format() 메소드 사용
print('Name: {}, Age: {}'.format(name, age))

# f-string 사용 (파이썬 3.6 이상)
print(f'Name: {name}, Age: {age}')

# f-string 안에는 수식도 사용 가능
radius = 5.0
print(f'Area of circle: {3.14 * radius ** 2}')

# --- 파이썬의 동적 타이핑 ---
x = 10 # x는 int 형
x = 'hello' # 이제 x는 str 형 (오류 없음)

# --- C 언어의 정적 타이핑 ---
// C 언어 예제
int x = 10; /* x를 int 형으로 선언 */
x = "hello"; /* 컴파일 오류! 자료형 불일치 */

# ============================================================
# 실습을 통한 2장 개념 정리
# ============================================================

radius = 8.0
print('Radius        :', radius)
print('Area          :', 3.14 * radius * radius)
print('Circumference :', 2.0 * 3.14 * radius)

width = 100
height = 200
print('Area :', width * height)

s = 'Hello Python'
print(s[6:])         # 'Python'

s = 'I like Java'
print(s.replace('Java', 'Python'))

last_name  = 'Hong'
first_name = 'Gildong'
print(f'제 이름은 {last_name} {first_name}입니다.')

x1 = 1
y1 = 2
x2 = 5
y2 = 6
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print('Distance :', distance)

total = 7384         # 초 단위 시간
hours   = total // 3600
minutes = (total % 3600) // 60
seconds = total % 60
print(f'{hours}h {minutes}m {seconds}s')

n = 1234
d1 = n // 1000           # 천의 자리
d2 = (n // 100) % 10     # 백의 자리
d3 = (n // 10) % 10      # 십의 자리
d4 = n % 10              # 일의 자리
print('Sum of digits :', d1 + d2 + d3 + d4)

s = 'level'
print(f'"{s}" is palindrome? {s == s[::-1]}')

s = 'python'
print(f'"{s}" is palindrome? {s == s[::-1]}')
