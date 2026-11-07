# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제6장 딕셔너리, 튜플, 집합
# 코드 6.3: 딕셔너리 항목의 추가·수정·삭제

person = {'이름': '홍길동', '나이': 26, '몸무게': 82}

# 항목 추가
person['직업'] = '율도국 왕'
print(person)

# 항목 수정
person['나이'] = 27
print(person)

# 항목 삭제
del person['몸무게']
print(person)
