# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.8: 생성자와 인스턴스 변수

class Cat:
    # 생성자 -- 인스턴스가 생성될 때 자동으로 호출됨
    def __init__(self, name, color):
        self.name = name # 인스턴스 변수
        self.color = color # 인스턴스 변수

    def meow(self):
        print(f'My name is {self.name}, color is {self.color}, meow~~')

nabi = Cat('Nabi', 'black') # nabi 인스턴스
nero = Cat('Nero', 'white') # nero 인스턴스
mimi = Cat('Mimi', 'brown') # mimi 인스턴스

nabi.meow() # My name is Nabi, color is black, meow~~
nero.meow() # My name is Nero, color is white, meow~~
mimi.meow() # My name is Mimi, color is brown, meow~~
