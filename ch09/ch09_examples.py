"""
제9장: 클래스와 객체
알짜 파이썬 — 예제 코드 (원고에서 자동 추출)
"""

# ============================================================
# 객체 지향 프로그래밍과 객체
# ============================================================

# --- 리스트와 문자열 객체의 메소드 ---
animals = ['lion', 'tiger', 'cat', 'dog']
animals.sort() # 리스트 객체의 sort() 메소드
animals.append('rabbit') # 리스트 객체의 append() 메소드
print(animals)
# ['cat', 'dog', 'lion', 'tiger', 'rabbit']

s = 'tiger'
print(s.upper()) # 문자열 객체의 upper() 메소드 -- 'TIGER'
print(s.find('g')) # 문자열 객체의 find() 메소드 -- 2

# --- type()과 id()로 객체의 타입과 ID 확인 ---
animals = ['lion', 'tiger', 'cat', 'dog']
print(type(animals)) # <class 'list'>
print(id(animals)) # 24990662 (고유한 아이디)

s = 'tiger'
print(type(s)) # <class 'str'>
print(id(s)) # 83596600

n = 200
print(type(n)) # <class 'int'>
print(id(n)) # 24990565

# --- 정수도 객체이며 더하기 메소드를 가짐 ---
n = 200
print(type(n)) # <class 'int'>
print(id(n)) # 24990565
print(n + 100) # 300
print(n.__add__(100)) # 300 (n + 100과 동일)
print(200 + 100) # 300
print((200).__add__(100)) # 300 (200 + 100과 동일)

# ============================================================
# 클래스 정의와 객체 생성
# ============================================================

# --- class 키워드로 클래스 정의 문법 ---
class ClassName:
    <statement-1>
    ...
    <statement-n>

# --- 빈 Cat 클래스 정의와 인스턴스 생성 ---
class Cat: # Cat 클래스 정의
    pass # 추후 코드를 위한 자리 표시자

nabi = Cat() # Cat 클래스의 인스턴스 생성
print(nabi) # <__main__.Cat object at 0x7f78399e0eb8>
print(type(nabi)) # <class '__main__.Cat'>

class Cat:
    def meow(self): # Cat 클래스의 메소드
        print('Meow meow~~~')

nabi = Cat()
nabi.meow() # Meow meow~~~

class Cat:
    def meow(self):
        print('Meow meow~~~')

nabi = Cat()
nabi.meow() # Meow meow~~~
nero = Cat()
nero.meow() # Meow meow~~~
mimi = Cat()
mimi.meow() # Meow meow~~~

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

# --- 학생 정보를 관리하는 Student 클래스 ---
class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    def info(self):
        avg = self.average()
        print(f'{self.name}({self.student_id}) - {self.major}, avg: {avg:.1f}')

# 학생 객체를 생성하고 사용
s1 = Student('Hong Gildong', '2026001', 'Computer Science')
s1.add_score(85)
s1.add_score(92)
s1.add_score(78)
s1.info() # Hong Gildong(2026001) - Computer Science, avg: 85.0

s2 = Student('Kim Younghee', '2026002', 'Business')
s2.add_score(95)
s2.add_score(88)
s2.info() # Kim Younghee(2026002) - Business, avg: 91.5

# ============================================================
# 클래스 변수와 캡슐화
# ============================================================

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

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # 외부에서 직접 접근 제한

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited {amount}. Balance: {self.__balance}')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdrew {amount}. Balance: {self.__balance}')
        else:
            print('Insufficient balance.')

    def get_balance(self):
        return self.__balance

acc = BankAccount('Hong Gildong', 100000)
acc.deposit(50000) # Deposited 50000. Balance: 150000
acc.withdraw(30000) # Withdrew 30000. Balance: 120000
print(acc.get_balance()) # 120000

# acc.__balance # AttributeError! 직접 접근 불가

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'Cat({self.name}, {self.color})'

nabi = Cat('Nabi', 'black')
print(nabi) # Cat(Nabi, black)

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

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self): # 속성처럼 사용됨
        return self.__balance

    @balance.setter
    def balance(self, value): # 값을 대입할 때 호출됨
        if value < 0:
            print('Balance cannot be negative.')
            return
        self.__balance = value

acc = BankAccount('Hong Gildong', 100000)
print(acc.balance) # 100000 -- 괄호 없이 접근
acc.balance = 50000 # 세터가 실행되어 값을 검증
print(acc.balance) # 50000
acc.balance = -1000 # 세터가 거부

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text): # 'Nabi,3' -> Cat('Nabi', 3)
        name, age = text.split(',')
        return cls(name, int(age))

c1 = Cat('Choco', 2) # 기본 생성자
c2 = Cat.from_string('Nabi,3') # 대안 생성자
print(c1.name, c1.age) # Choco 2
print(c2.name, c2.age) # Nabi 3

# ============================================================
# 상속의 활용 — super()와 다형성
# ============================================================

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

class Duck:
    def speak(self):
        print('Quack!')

class Person:
    def speak(self):
        print('Hello!')

# 공통 부모는 없지만 둘 다 동일하게 처리 가능
for obj in [Duck(), Person()]:
    obj.speak()

# ============================================================
# 실습을 통한 9장 개념 정리
# ============================================================

class Rectangle:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(3, 5)
print('Area      :', r.area())        # 15
print('Perimeter :', r.perimeter())   # 16

class Student:
    def __init__(self, name, scores):
        self.name   = name
        self.scores = scores
    def average(self):
        return sum(self.scores) / len(self.scores)
    def show(self):
        print(f'{self.name} : avg={self.average():.1f}')

s = Student('Hong', [85, 90, 78])
s.show()            # Hong : avg=84.3

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f'{self.name}: ...')

class Dog(Animal):
    def speak(self):
        print(f'{self.name}: Woof!')

class Cat(Animal):
    def speak(self):
        print(f'{self.name}: Meow~')

for a in [Dog('Baduk'), Cat('Nabi')]:
    a.speak()

from datetime import date
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year
    def age(self):
        return date.today().year - self.year
    def info(self):
        print(f'{self.year} {self.brand} {self.model} ({self.age()} years)')

c = Car('Hyundai', 'Sonata', 2020)
c.info()
