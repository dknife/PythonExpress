# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.18: 예측과 회귀선 시각화

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 코드 12.17의 데이터와 모델 준비
np.random.seed(42)
study_hours = np.random.uniform(1, 10, 30)
scores = study_hours * 8 + np.random.normal(0, 5, 30) + 20
X = study_hours.reshape(-1, 1)
y = scores
model = LinearRegression().fit(X, y)
a = model.coef_[0]
b = model.intercept_

# 새로운 공부 시간에 대한 점수 예측
new_hours = np.array([[4.5], [6.5], [10]])
predictions = model.predict(new_hours)

print('Predictions:')
for h, s in zip(new_hours.flatten(), predictions):
    print(f' Study {h:.1f} hours -> {s:.1f} points')

# 그래프: 산점도 + 회귀선
plt.figure(figsize=(8, 5))

# 원본 데이터 (산점도)
plt.scatter(study_hours, scores, color='steelblue', s=80,
    edgecolors='navy', label='Actual data', zorder=3)

# 회귀선
line_x = np.linspace(0, 10, 100).reshape(-1, 1)
line_y = model.predict(line_x)
plt.plot(line_x, line_y, color='red', linewidth=2,
    label=f'Fit line: y={a:.2f}x+{b:.2f}')

# 예측된 점
plt.scatter(new_hours, predictions, color='red', s=120,
    marker='*', zorder=4, label='Predicted')

plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.title('Linear Regression: Study Hours vs Score')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, 11)
plt.ylim(20, 105)
plt.show()
