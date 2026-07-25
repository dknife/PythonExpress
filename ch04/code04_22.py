# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.22: 0으로 자리를 채운 정렬 출력

n = int(input('How many numbers? '))
print('---- formatted ----')
for _ in range(n):
    x = float(input('Enter a number: '))
    print(f'{x:08.2f}') # 전체 폭 8자리, 빈 자리는 0으로 채움
