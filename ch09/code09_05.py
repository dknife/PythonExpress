# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제9장 클래스와 객체
# 코드 9.5: 빈 Cat 클래스 정의와 인스턴스 생성

class Cat: # Cat 클래스 정의
    pass # 추후 코드를 위한 자리 표시자

nabi = Cat() # Cat 클래스의 인스턴스 생성
print(nabi) # <__main__.Cat object at 0x7f78399e0eb8>
print(type(nabi)) # <class '__main__.Cat'>
