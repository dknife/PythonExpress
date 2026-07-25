# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제6장 딕셔너리, 튜플, 집합
# 코드 6.3: 딕셔너리 항목의 추가·수정·삭제

person = {'name': 'Hong Gildong', 'age': 26, 'weight': 82}

# 항목 추가
person['job'] = 'King of Yuldo'
print(person)

# 항목 수정
person['age'] = 27
print(person)

# 항목 삭제
del person['weight']
print(person)
