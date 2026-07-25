# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.10: 클래스 변수로 인스턴스 수 추적하기

class Dog:
    count = 0 # 클래스 변수 -- 모든 인스턴스가 공유

    def __init__(self, name):
        self.name = name # 인스턴스 변수 -- 인스턴스마다 고유
        Dog.count += 1 # 객체가 생성될 때마다 1씩 증가

    def bark(self):
        print(f'{self.name}: Woof woof~~!!')

d1 = Dog('Baduk')
d2 = Dog('Choco')
d3 = Dog('Jindol')

print(f'Number of dogs created: {Dog.count}') # 3
d1.bark() # Baduk: Woof woof~~!!
d2.bark() # Choco: Woof woof~~!!
