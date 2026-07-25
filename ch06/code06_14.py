# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제6장 딕셔너리, 튜플, 집합
# 코드 6.14: 리스트·튜플·집합 간 변환

# 리스트 -> 튜플 -> 집합 변환
my_list = [1, 2, 3, 2, 1]

my_tuple = tuple(my_list)
print('Tuple:', my_tuple)

my_set = set(my_list)
print('Set:', my_set)

back_to_list = list(my_set)
print('List:', back_to_list)
