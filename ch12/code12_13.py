# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.13: 시험 점수 분포 히스토그램

import numpy as np
import matplotlib.pyplot as plt

# 평균 70, 표준편차 10인 난수 점수 200개 생성
scores = np.random.normal(70, 10, 200)

plt.figure(figsize=(7, 4))
plt.hist(scores, bins=15, color='#4CAF50', edgecolor='white',
    alpha=0.8)
plt.title('Exam Score Distribution', fontsize=14)
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.axvline(scores.mean(), color='red', linestyle='--',
    label=f'Mean: {scores.mean():.1f}')
plt.legend()
plt.tight_layout()
plt.show()
