# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.9: finally로 항상 실행되는 블록

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('0으로 나누기 오류')
    else:
        print('결과:', result)
    finally:
        print('완료')

print('divide(100, 2) 호출:')
divide(100, 2)
print('divide(100, 0) 호출:')
divide(100, 0)
