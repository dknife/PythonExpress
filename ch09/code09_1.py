# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.1: 리스트와 문자열 객체의 메소드

animals = ['lion', 'tiger', 'cat', 'dog']
animals.sort() # 리스트 객체의 sort() 메소드
animals.append('rabbit') # 리스트 객체의 append() 메소드
print(animals)
# ['cat', 'dog', 'lion', 'tiger', 'rabbit']

s = 'tiger'
print(s.upper()) # 문자열 객체의 upper() 메소드 -- 'TIGER'
print(s.find('g')) # 문자열 객체의 find() 메소드 -- 2
