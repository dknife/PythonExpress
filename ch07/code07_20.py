# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.20: random 모듈의 기본 난수 함수

import random as rd

print(rd.random()) # 0.0 이상 1.0 미만의 실수
print(rd.randint(1, 6)) # 1 이상 6 이하의 정수 (주사위)
print(rd.randrange(0, 10)) # 0 이상 9 이하의 정수
