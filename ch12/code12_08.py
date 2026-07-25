# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.8: dropna()로 결측값 행 삭제

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

df_dropped = df.dropna()
print('dropna result:')
print(df_dropped)
