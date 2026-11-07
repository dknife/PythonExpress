# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.8: else로 정상 실행 결과 출력

try:
    a, b = input('두 수를 입력하세요: ').split()
    result = int(a) / int(b)
except ZeroDivisionError:
    print('오류: 0으로 나눌 수 없습니다.')
except ValueError:
    print('오류: 정수를 입력하세요.')
except:
    print('오류: 10 2처럼 두 수를 입력하세요.')
else: # 예외가 없을 때만 실행
    print('{} / {} = {}'.format(a, b, result))
