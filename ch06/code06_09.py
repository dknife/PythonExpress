# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제6장 딕셔너리, 튜플, 집합
# 코드 6.9: 튜플로 두 값 동시 반환

def get_min_max(numbers):
    return min(numbers), max(numbers) # 튜플로 반환

data = [45, 23, 78, 12, 67]
minimum, maximum = get_min_max(data)
print(f'Min: {minimum}, Max: {maximum}')
