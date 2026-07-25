# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.14: @property로 게터·세터를 속성처럼 사용

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
