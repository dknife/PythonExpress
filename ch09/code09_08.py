# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.8: 생성자와 인스턴스 변수

class Cat:
    # 생성자 -- 인스턴스가 생성될 때 자동으로 호출됨
    def __init__(self, name, color):
        self.name = name # 인스턴스 변수
        self.color = color # 인스턴스 변수

    def meow(self):
        print(f'내 이름은 {self.name}, 색깔은 {self.color}, 야옹~~')

nabi = Cat('나비', '검은색') # nabi 인스턴스
nero = Cat('네로', '흰색') # nero 인스턴스
mimi = Cat('미미', '갈색') # mimi 인스턴스

nabi.meow() # 내 이름은 나비, 색깔은 검은색, 야옹~~
nero.meow() # 내 이름은 네로, 색깔은 흰색, 야옹~~
mimi.meow() # 내 이름은 미미, 색깔은 갈색, 야옹~~
