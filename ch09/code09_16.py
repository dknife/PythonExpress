# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.16: super()로 부모 생성자 호출

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'{self.name} ({self.age} years old)')

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age) # 부모의 __init__ 호출
        self.breed = breed # 자식만의 속성 추가

    def info(self):
        super().info() # 부모의 info()를 확장
        print(f' Breed: {self.breed}')

baduk = Dog('Baduk', 3, 'Jindo')
baduk.info()
