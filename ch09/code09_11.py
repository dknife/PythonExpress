# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.11: 캡슐화로 은행 계좌 보호하기

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
