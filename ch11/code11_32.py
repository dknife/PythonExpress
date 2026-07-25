# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제11장 파이썬다운 코딩과 넘파이
# 코드 11.32: 배열의 최댓값·평균·합 메소드

import numpy as np

data = np.array([23, 45, 67, 7, 2, 30, 34, 82])
print('Max :', data.max())
print('Min :', data.min())
print('Mean :', data.mean())
print('Sum :', data.sum())
print('Sort :', np.sort(data))
