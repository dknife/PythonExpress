# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.7: 구체적 예외와 일반 Exception을 함께 처리

try:
# b = 2 / 0
    a = 1 + 'hundred'
except ZeroDivisionError: # 0으로 나누기 예외 처리
    print('Division by zero error')
except TypeError: # 지원되지 않는 자료형 연산 처리
    print('Unsupported operand type error')
except Exception as e: # 그 밖의 모든 예외 처리
    print('error :', e)
    print('Please check division and operand types.')
