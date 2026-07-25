# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.18: 덕 타이핑으로 상속 없이 공통 처리

class Duck:
    def speak(self):
        print('Quack!')

class Person:
    def speak(self):
        print('Hello!')

# 공통 부모는 없지만 둘 다 동일하게 처리 가능
for obj in [Duck(), Person()]:
    obj.speak()
