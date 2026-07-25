# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제11장 파이썬다운 코딩과 넘파이
# 코드 11.23: 다양한 배열 생성 함수

import numpy as np

print(np.zeros(5)) # 0으로 채운 배열
print(np.ones((2, 3))) # 1로 채운 2x3 배열
print(np.arange(0, 10, 2)) # 0부터 10 미만까지 간격 2
print(np.linspace(0, 1, 5)) # 0부터 1까지 균등 간격 값 5개
print(np.random.rand(3)) # 0과 1 사이의 난수 3개
print(np.random.randint(0, 10, size=5)) # 0~9 범위의 정수 난수 5개
