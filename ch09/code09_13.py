# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.13: Animal 상속과 speak 메소드 오버라이딩

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} makes a sound.')

class Dog(Animal): # Animal 클래스를 상속
    def speak(self): # 메소드 오버라이딩
        print(f'{self.name}: Woof!')

class Cat(Animal): # Animal 클래스를 상속
    def speak(self): # 메소드 오버라이딩
        print(f'{self.name}: Meow~')

dog = Dog('Baduk')
cat = Cat('Nabi')
dog.speak() # Baduk: Woof!
cat.speak() # Nabi: Meow~
