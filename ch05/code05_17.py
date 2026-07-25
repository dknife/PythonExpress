# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제5장 리스트와 슬라이싱
# 코드 5.17: input으로 리스트 구성하기

names = [] # 빈 리스트 생성

for i in range(3):
    name = input(f'Name {i+1}: ')
    names.append(name)

print('Entered names:', names)
