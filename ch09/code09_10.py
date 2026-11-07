# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.10: 클래스 변수로 인스턴스 수 추적하기

class Dog:
    count = 0 # 클래스 변수 -- 모든 인스턴스가 공유

    def __init__(self, name):
        self.name = name # 인스턴스 변수 -- 인스턴스마다 고유
        Dog.count += 1 # 객체가 생성될 때마다 1씩 증가

    def bark(self):
        print(f'{self.name}: 멍멍~~!!')

d1 = Dog('바둑')
d2 = Dog('초코')
d3 = Dog('진돌')

print(f'생성된 강아지 수: {Dog.count}') # 3
d1.bark() # 바둑: 멍멍~~!!
d2.bark() # 초코: 멍멍~~!!
