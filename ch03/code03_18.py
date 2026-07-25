# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.18: continue 문으로 홀수만 출력  —  continue_test.py

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print()
