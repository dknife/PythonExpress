# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.4: try-except로 나눗셈 오류 처리

try:
    a, b = input('두 수를 입력하세요: ').split()
    result = int(a) / int(b)
    print('{}/{} = {}'.format(a, b, result))
except:
    print('수가 정확한지 확인하세요.')
