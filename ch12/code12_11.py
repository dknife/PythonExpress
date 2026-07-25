# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.11: groupby()로 학년별 평균 구하기

import pandas as pd
import numpy as np

# 코드 12.6의 df 준비
df = pd.DataFrame({
    'name': ['Hong Gildong', 'Kim Cheolsu', 'Lee Younghee',
        'Park Jimin', 'Choi Suhyun'],
    'year': [1, 2, 1, 3, 2],
    'Korean': [85, 92, np.nan, 95, 78],
    'English': [90, np.nan, 82, 91, 88],
    'Math': [78, 95, 88, np.nan, 92]
})

# 학년별 국어 점수 평균
print(df.groupby('year')['Korean'].mean())

# 학년별 모든 수치형 열의 평균
print(df.groupby('year')[['Korean', 'English', 'Math']].mean())
