# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.9: finally로 항상 실행되는 블록

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Division by zero error')
    else:
        print('Result:', result)
    finally:
        print('Done')

print('divide(100, 2) call:')
divide(100, 2)
print('divide(100, 0) call:')
divide(100, 0)
