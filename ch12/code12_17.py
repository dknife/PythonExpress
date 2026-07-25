# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.17: 선형 회귀 모델 학습

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 코드 12.14에서 사용한 데이터
np.random.seed(42)
study_hours = np.random.uniform(1, 10, 30)
scores = study_hours * 8 + np.random.normal(0, 5, 30) + 20

# reshape: 사이킷런의 특성 데이터는 2차원 배열이어야 함
X = study_hours.reshape(-1, 1) # (30, 1) 열 벡터
y = scores

# 모델 학습
model = LinearRegression()
model.fit(X, y)

# 모델 파라미터
a = model.coef_[0] # 기울기
b = model.intercept_ # 절편
print(f'Regression line: y = {a:.2f}x + {b:.2f}')
