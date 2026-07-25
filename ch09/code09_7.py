# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.7: 여러 인스턴스가 같은 메소드 공유

class Cat:
    def meow(self):
        print('Meow meow~~~')

nabi = Cat()
nabi.meow() # Meow meow~~~
nero = Cat()
nero.meow() # Meow meow~~~
mimi = Cat()
mimi.meow() # Meow meow~~~
