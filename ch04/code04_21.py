# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.21: input()으로 받은 숫자를 f-string으로 정렬 출력

n = int(input('How many numbers? '))
print('---- formatted ----')
for _ in range(n):
    x = float(input('Enter a number: '))
    print(f'{x:7.2f}') # 전체 폭 7자리, 소수점 2자리
