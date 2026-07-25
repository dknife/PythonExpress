# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제3장 조건문과 반복문
# 코드 3.14: 이중 for 문으로 구구단 전체 출력  —  double_for.py

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i}*{j}={i*j:2d}', end=' ')
    print()
