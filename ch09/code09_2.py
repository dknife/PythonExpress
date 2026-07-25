# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.2: type()과 id()로 객체의 타입과 ID 확인

animals = ['lion', 'tiger', 'cat', 'dog']
print(type(animals)) # <class 'list'>
print(id(animals)) # 24990662 (고유한 아이디)

s = 'tiger'
print(type(s)) # <class 'str'>
print(id(s)) # 83596600

n = 200
print(type(n)) # <class 'int'>
print(id(n)) # 24990565
