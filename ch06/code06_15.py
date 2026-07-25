# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제6장 딕셔너리, 튜플, 집합
# 코드 6.15: 딕셔너리를 리스트로 변환

person = {'name': 'Hong Gildong', 'age': 26}

print(list(person)) # 키의 리스트
print(list(person.values())) # 값의 리스트
print(list(person.items())) # (키, 값) 튜플의 리스트
