# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.19: 반복문과 조건문을 조합한 짝수/홀수 합

even_sum = 0
odd_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f'짝수의 합: {even_sum}')
print(f'홀수의 합: {odd_sum}')
