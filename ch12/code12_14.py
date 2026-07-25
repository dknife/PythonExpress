# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.14: 공부 시간과 점수의 산점도

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
study_hours = np.random.uniform(1, 10, 30)
scores = study_hours * 8 + np.random.normal(0, 5, 30) + 20

plt.figure(figsize=(7, 4))
plt.scatter(study_hours, scores, color='#FF5722', alpha=0.7,
    edgecolors='black', linewidth=0.5)
plt.title('Study Hours and Score Relation', fontsize=14)
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
