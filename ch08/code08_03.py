# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.3: 숫자가 아닌 입력으로 인한 ValueError

a, b = input('Enter two numbers: ').split()
result = int(a) / int(b)
