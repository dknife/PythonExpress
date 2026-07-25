# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제11장 파이썬다운 코딩과 넘파이
# 코드 11.11: for 문으로 리스트 요소 제곱하기

a = [1, 2, 3, 4, 5, 6, 7]
square_a = []
for n in a:
    square_a.append(n ** 2) # n의 제곱을 square_a 리스트에 추가
print(square_a)
