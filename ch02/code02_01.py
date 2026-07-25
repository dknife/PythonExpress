# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제2장 변수, 연산자, 문자열
# 코드 2.1: print() 함수의 end와 sep 인자

# end 인자: 출력 후 줄 바꿈 대신 공백 사용
print('Hello', end=' ')
print('Python!')

# sep 인자: 값 사이의 구분 문자를 '-'로 변경
print('2025', '04', '07', sep='-')

# sep과 end를 함께 사용
print('A', 'B', 'C', sep=', ', end='!\n')
