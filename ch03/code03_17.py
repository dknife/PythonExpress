# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.17: break 문으로 반복 중단  —  break_test.py

for i in range(1, 11):
    if i == 6:
        break
    print(i, end=' ')
print()
print('Loop ended')
