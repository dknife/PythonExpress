# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제6장 딕셔너리, 튜플, 집합
# 코드 6.11: set()으로 리스트 중복 제거

numbers = [1, 3, 2, 3, 1, 5, 2, 4, 5]
unique = list(set(numbers))
print(unique)
