# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.9: fillna()로 결측값 채우기

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

# 0으로 채우기
df_filled = df.fillna(0)
print('fillna(0) result:')
print(df_filled)

# 열 평균으로 채우기 (더 합리적)
df_mean = df.copy()
df_mean['Korean'] = df_mean['Korean'].fillna(
    df_mean['Korean'].mean())
df_mean['English'] = df_mean['English'].fillna(
    df_mean['English'].mean())
df_mean['Math'] = df_mean['Math'].fillna(
    df_mean['Math'].mean())
print('\nfillna(mean) result:')
print(df_mean)
