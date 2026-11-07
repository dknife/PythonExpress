# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.5: 예외 종류별로 나누어 처리하기

try:
    b = 2 / 0
    a = 1 + '백'
except ZeroDivisionError:
    print('0으로 나누기 오류')
except TypeError:
    print('지원되지 않는 피연산자 자료형 오류')
