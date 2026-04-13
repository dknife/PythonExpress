"""
제9장: 클래스와 객체
으뜸 파이썬 Express — 예제 코드
"""

# ============================================================
# 객체 지향 프로그래밍과 객체
# ============================================================

animals = ['lion', 'tiger', 'cat', 'dog']
animals.sort()              # sort() method of list object
animals.append('rabbit')    # append() method of list object
print(animals)
# ['cat', 'dog', 'lion', 'tiger', 'rabbit']

s = 'tiger'
print(s.upper())   # upper() method of str object -- 'TIGER'
print(s.find('g')) # find() method of str object -- 2

animals = ['lion', 'tiger', 'cat', 'dog']
print(type(animals))  # <class 'list'>
print(id(animals))    # 24990662 (unique id)

s = 'tiger'
print(type(s))        # <class 'str'>
print(id(s))          # 83596600

n = 200
print(type(n))        # <class 'int'>
print(id(n))          # 24990565

n = 200
print(type(n))            # <class 'int'>
print(id(n))              # 24990565
print(n + 100)            # 300
print(n.__add__(100))     # 300 (same as n + 100)
print(200 + 100)          # 300
print((200).__add__(100)) # 300 (same as 200 + 100)

# ============================================================
# 클래스 정의와 객체 생성
# ============================================================

class ClassName:
    <statement-1>
    ...
    <statement-n>

class Cat:       # define Cat class
    pass         # placeholder for future code

nabi = Cat()     # create an instance of Cat
print(nabi)      # <__main__.Cat object at 0x7f78399e0eb8>
print(type(nabi)) # <class '__main__.Cat'>

class Cat:
    def meow(self):    # Cat class method
        print('Meow meow~~~')

nabi = Cat()
nabi.meow()  # Meow meow~~~

class Cat:
    def meow(self):
        print('Meow meow~~~')

nabi = Cat()
nabi.meow()    # Meow meow~~~
nero = Cat()
nero.meow()    # Meow meow~~~
mimi = Cat()
mimi.meow()    # Meow meow~~~

class Cat:
    # constructor -- called automatically when instance is created
    def __init__(self, name, color):
        self.name = name    # instance variable
        self.color = color  # instance variable

    def meow(self):
        print(f'My name is {self.name}, color is {self.color}, meow~~')

nabi = Cat('Nabi', 'black')    # nabi instance
nero = Cat('Nero', 'white')    # nero instance
mimi = Cat('Mimi', 'brown')    # mimi instance

nabi.meow()  # My name is Nabi, color is black, meow~~
nero.meow()  # My name is Nero, color is white, meow~~
mimi.meow()  # My name is Mimi, color is brown, meow~~

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

# create and use student objects
s1 = Student('Hong Gildong', '2026001', 'Computer Science')
s1.add_score(85)
s1.add_score(92)
s1.add_score(78)
s1.info()  # Hong Gildong(2026001) - Computer Science, avg: 85.0

s2 = Student('Kim Younghee', '2026002', 'Business')
s2.add_score(95)
s2.add_score(88)
s2.info()  # Kim Younghee(2026002) - Business, avg: 91.5

# ============================================================
# 클래스 변수와 캡슐화
# ============================================================

class Dog:
    count = 0  # class variable -- shared by all instances

    def __init__(self, name):
        self.name = name      # instance variable -- unique to each
        Dog.count += 1        # incremented each time an object is created

    def bark(self):
        print(f'{self.name}: Woof woof~~!!')

d1 = Dog('Baduk')
d2 = Dog('Choco')
d3 = Dog('Jindol')

print(f'Number of dogs created: {Dog.count}')  # 3
d1.bark()  # Baduk: Woof woof~~!!
d2.bark()  # Choco: Woof woof~~!!

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # restricted from outside access

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
acc.deposit(50000)    # Deposited 50000. Balance: 150000
acc.withdraw(30000)   # Withdrew 30000. Balance: 120000
print(acc.get_balance())  # 120000

# acc.__balance  # AttributeError! Cannot access directly

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'Cat({self.name}, {self.color})'

nabi = Cat('Nabi', 'black')
print(nabi)  # Cat(Nabi, black)

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} makes a sound.')

class Dog(Animal):          # inherits Animal class
    def speak(self):        # method overriding
        print(f'{self.name}: Woof!')

class Cat(Animal):          # inherits Animal class
    def speak(self):        # method overriding
        print(f'{self.name}: Meow~')

dog = Dog('Baduk')
cat = Cat('Nabi')
dog.speak()  # Baduk: Woof!
cat.speak()  # Nabi: Meow~
