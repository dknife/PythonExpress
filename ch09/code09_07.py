# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.7: 여러 인스턴스가 같은 메소드 공유

class Cat:
    def meow(self):
        print('야옹 야옹~~~')

nabi = Cat()
nabi.meow() # 야옹 야옹~~~
nero = Cat()
nero.meow() # 야옹 야옹~~~
mimi = Cat()
mimi.meow() # 야옹 야옹~~~
