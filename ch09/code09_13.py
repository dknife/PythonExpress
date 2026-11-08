# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.13: Animal 상속과 speak 메소드 오버라이딩

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name}: 소리를 냅니다.')

class Dog(Animal):    # Animal 클래스를 상속
    def speak(self):  # 메소드 오버라이딩
        print(f'{self.name}: 멍멍!')

class Cat(Animal):    # Animal 클래스를 상속
    def speak(self):  # 메소드 오버라이딩
        print(f'{self.name}: 야옹~')

dog = Dog('바둑')
cat = Cat('나비')
dog.speak()  # 바둑: 멍멍!
cat.speak()  # 나비: 야옹~
