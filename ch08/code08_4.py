# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.4: try-except로 나눗셈 오류 처리

try:
    a, b = input('Enter two numbers: ').split()
    result = int(a) / int(b)
    print('{}/{} = {}'.format(a, b, result))
except:
    print('Please check if the numbers are correct.')
