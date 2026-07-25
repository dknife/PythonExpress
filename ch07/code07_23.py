# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.23: numpy 배열 연산의 간결함

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a * 2) # [2 4 6 8 10] -- 요소별 곱셈
print(a.mean()) # 3.0 -- 평균
print(a.sum()) # 15 -- 합계
