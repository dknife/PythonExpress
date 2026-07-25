# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제5장 리스트와 슬라이싱
# 코드 5.19: index(), count(), insert() 활용

a_list = ['a', 'b', 'c', 'd', 'e']
print(a_list.index('c')) # 2
print(a_list.count('a')) # 1

a_list.insert(1, 'x') # 인덱스 1 위치에 'x' 삽입
print(a_list)
