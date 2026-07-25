# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.12: 객체의 문자열 표현 정의

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'Cat({self.name}, {self.color})'

nabi = Cat('Nabi', 'black')
print(nabi) # Cat(Nabi, black)
