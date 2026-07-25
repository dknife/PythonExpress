# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제11장 파이썬다운 코딩과 넘파이
# 코드 11.33: flatten()으로 2차원 배열 평탄화

import numpy as np

a = np.array([[1, 1], [2, 2], [3, 3]])
print(a.flatten()) # 1차원 배열로 평탄화
