# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.17: 다형성으로 여러 동물 한 번에 처리

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f'{self.name} makes a sound.')

class Dog(Animal):
    def speak(self):
        print(f'{self.name}: Woof!')

class Cat(Animal):
    def speak(self):
        print(f'{self.name}: Meow~')

class Cow(Animal):
    def speak(self):
        print(f'{self.name}: Moo~')

# 같은 인터페이스로 모든 동물을 동일하게 처리
animals = [Dog('Baduk'), Cat('Nabi'), Cow('Worky')]
for a in animals:
    a.speak()
