# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.1: 구문 오류의 대표적인 예

# 닫는 따옴표 누락 -- 구문 오류
print('Hello World!)
# SyntaxError: EOL while scanning string literal

# if 문 뒤에 콜론 누락
if True
    print('hello')
# SyntaxError: expected ':'
