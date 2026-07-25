# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.6: 클래스에 메소드 추가하기

class Cat:
    def meow(self): # Cat 클래스의 메소드
        print('Meow meow~~~')

nabi = Cat()
nabi.meow() # Meow meow~~~
