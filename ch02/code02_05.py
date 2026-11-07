# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제2장 변수, 연산자, 문자열
# 코드 2.5: 문자열 포매팅

name = '홍길동'
age = 27

# format() 메소드 사용
print('이름: {}, 나이: {}'.format(name, age))

# f-string 사용 (파이썬 3.6 이상)
print(f'이름: {name}, 나이: {age}')

# f-string 안에는 수식도 사용 가능
radius = 5.0
print(f'원의 면적: {3.14 * radius ** 2}')
