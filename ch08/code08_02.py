# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.2: 0으로 나누기로 인한 ZeroDivisionError

a, b = input('Enter two numbers: ').split()
result = int(a) / int(b) # b가 0이면 ZeroDivisionError 발생!
