# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제6장 딕셔너리, 튜플, 집합
# 코드 6.13: add, remove, discard 메소드

s = {1, 2, 3}

s.add(4) # 원소 추가
print(s)

s.remove(2) # 원소 삭제 (없으면 KeyError)
print(s)

s.discard(99) # 원소 삭제 (없어도 오류 없음)
print(s)

print(3 in s) # 원소 존재 확인: True
