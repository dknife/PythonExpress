# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.7: 구체적 예외와 일반 Exception을 함께 처리

try:
# b = 2 / 0
    a = 1 + '백'
except ZeroDivisionError: # 0으로 나누기 예외 처리
    print('0으로 나누기 오류')
except TypeError: # 지원되지 않는 자료형 연산 처리
    print('지원되지 않는 피연산자 자료형 오류')
except Exception as e: # 그 밖의 모든 예외 처리
    print('오류:', e)
    print('나눗셈과 피연산자 자료형을 확인하세요.')
