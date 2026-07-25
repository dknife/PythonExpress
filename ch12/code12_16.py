# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.16: DataFrame에서 직접 막대 그래프 그리기

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'name': ['Hong', 'Kim', 'Lee', 'Park'],
    'Korean': [85, 92, 78, 95],
    'English': [90, 88, 82, 91],
    'Math': [78, 95, 88, 87]
})
df.set_index('name')[['Korean', 'English', 'Math']].plot.bar(
    figsize=(7, 4), rot=0, edgecolor='white')
plt.title('Student Scores by Subject', fontsize=14)
plt.ylabel('Score')
plt.ylim(0, 100)
plt.legend(loc='lower right')
plt.tight_layout()
plt.show()
