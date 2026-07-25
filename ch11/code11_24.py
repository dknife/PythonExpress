# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제11장 파이썬다운 코딩과 넘파이
# 코드 11.24: 리스트와 넘파이의 실행 시간 비교

import numpy as np
import time

n = 1_000_000

# 파이썬 리스트
py_list = list(range(n))
start = time.time()
result = [x**2 for x in py_list]
py_time = time.time() - start

# 넘파이 배열
np_arr = np.arange(n)
start = time.time()
result = np_arr ** 2
np_time = time.time() - start

print(f'List comprehension : {py_time:.4f} sec')
print(f'NumPy vectorization: {np_time:.4f} sec')
print(f'NumPy is {py_time/np_time:.1f}x faster')
