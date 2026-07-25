# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제6장 딕셔너리, 튜플, 집합
# 코드 6.12: 합집합·교집합·차집합·대칭차집합

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print('Union:', A | B) # 또는 A.union(B)
print('Intersection:', A & B) # 또는 A.intersection(B)
print('Difference:', A - B) # 또는 A.difference(B)
print('Symmetric diff:', A ^ B) # 또는 A.symmetric_difference(B)
