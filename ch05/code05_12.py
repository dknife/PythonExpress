# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제5장 리스트와 슬라이싱
# 코드 5.12: 반복문으로 합계와 평균 구하기

scores = [87, 84, 95, 67, 88]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print(f'Sum: {total}, Average: {average:.1f}')
