# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.16: 사용자 입력을 이용한 while 문  —  while_input.py

total = 0
count = 0
num = int(input('Enter a number (0 to quit): '))
while num != 0:
    total += num
    count += 1
    num = int(input('Enter a number (0 to quit): '))
if count > 0:
    print(f'Sum: {total}, Average: {total/count:.1f}')
else:
    print('No numbers were entered.')
