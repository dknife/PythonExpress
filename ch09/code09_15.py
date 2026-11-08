# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.15: @classmethod로 만드는 대안 생성자

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text): # '나비,3' -> Cat('나비', 3)
        name, age = text.split(',')
        return cls(name, int(age))

c1 = Cat('초코', 2)             # 기본 생성자
c2 = Cat.from_string('나비,3')  # 대안 생성자
print(c1.name, c1.age)          # 초코 2
print(c2.name, c2.age)          # 나비 3
