# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.12: 객체의 문자열 표현 정의

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'{self.color} 고양이 {self.name}'

nabi = Cat('나비', '검은색')
print(nabi) # 검은색 고양이 나비
