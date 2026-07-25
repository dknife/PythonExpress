# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.19: 결정계수로 모델 정확도 평가

import numpy as np
from sklearn.linear_model import LinearRegression

# 코드 12.17의 데이터와 모델 준비
np.random.seed(42)
study_hours = np.random.uniform(1, 10, 30)
scores = study_hours * 8 + np.random.normal(0, 5, 30) + 20
X = study_hours.reshape(-1, 1)
y = scores
model = LinearRegression().fit(X, y)

r2 = model.score(X, y)
print(f'R-squared: {r2:.4f}')
