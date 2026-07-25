# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제2장 변수, 연산자, 문자열
# 코드 2.5: 문자열 포매팅

name = 'Hong Gildong'
age = 27

# format() 메소드 사용
print('Name: {}, Age: {}'.format(name, age))

# f-string 사용 (파이썬 3.6 이상)
print(f'Name: {name}, Age: {age}')

# f-string 안에는 수식도 사용 가능
radius = 5.0
print(f'Area of circle: {3.14 * radius ** 2}')
