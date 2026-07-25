# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.8: else로 정상 실행 결과 출력

try:
    a, b = input('Enter two numbers: ').split()
    result = int(a) / int(b)
except ZeroDivisionError:
    print('Error: cannot divide by zero.')
except ValueError:
    print('Error: please enter integers.')
except:
    print('Error: enter two numbers like 10 2.')
else: # 예외가 없을 때만 실행
    print('{} / {} = {}'.format(a, b, result))
