# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제6장 딕셔너리, 튜플, 집합
# 코드 6.5: for 문으로 딕셔너리 순회

person = {'name': 'Hong Gildong', 'age': 26, 'weight': 82}

for key in person:
    print(f'{key} : {person[key]}')
