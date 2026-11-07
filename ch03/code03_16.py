# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.16: 사용자 입력을 이용한 while 문  —  while_input.py

total = 0
count = 0
num = int(input('숫자를 입력하세요(종료는 0): '))
while num != 0:
    total += num
    count += 1
    num = int(input('숫자를 입력하세요(종료는 0): '))
if count > 0:
    print(f'합계: {total}, 평균: {total/count:.1f}')
else:
    print('입력된 숫자가 없습니다.')
