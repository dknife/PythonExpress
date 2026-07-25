# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제11장 파이썬다운 코딩과 넘파이
# 코드 11.22: ndarray의 주요 속성 확인

import numpy as np

a = np.array([1, 2, 3])
print('shape :', a.shape) # 배열의 형상
print('ndim :', a.ndim) # 차원의 개수
print('dtype :', a.dtype) # 원소의 자료형
print('size :', a.size) # 전체 원소의 개수
print('itemsize:', a.itemsize) # 원소 하나의 바이트 크기
