# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제11장 파이썬다운 코딩과 넘파이
# 코드 11.32: 배열의 최댓값·평균·합 메소드

import numpy as np

data = np.array([23, 45, 67, 7, 2, 30, 34, 82])
print('최댓값:', data.max())
print('최솟값:', data.min())
print('평균:', data.mean())
print('합계:', data.sum())
print('정렬:', np.sort(data))
