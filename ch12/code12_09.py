# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.9: fillna()로 결측값 채우기

import pandas as pd
import numpy as np

# 코드 12.6의 df 준비
df = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희',
        '박지민', '최수현'],
    '학년': [1, 2, 1, 3, 2],
    '국어': [85, 92, np.nan, 95, 78],
    '영어': [90, np.nan, 82, 91, 88],
    '수학': [78, 95, 88, np.nan, 92]
})

# 0으로 채우기
df_filled = df.fillna(0)
print('fillna(0) 결과:')
print(df_filled)

# 열 평균으로 채우기 (더 합리적)
df_mean = df.copy()
df_mean['국어'] = df_mean['국어'].fillna(
    df_mean['국어'].mean())
df_mean['영어'] = df_mean['영어'].fillna(
    df_mean['영어'].mean())
df_mean['수학'] = df_mean['수학'].fillna(
    df_mean['수학'].mean())
print('\nfillna(평균) 결과:')
print(df_mean)
