# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.21: choice, shuffle, sample로 리스트 다루기

import random as rd

colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(rd.choice(colors)) # 리스트에서 무작위로 하나 선택

rd.shuffle(colors) # 리스트를 무작위로 섞기 (원본 변경)
print(colors) # 순서가 무작위로 바뀜

print(rd.sample(colors, 3)) # 3개를 비복원 추출
