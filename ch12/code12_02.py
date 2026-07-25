# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.2: 딕셔너리로 DataFrame 만들기

import pandas as pd

# DataFrame: 2차원 표 형태 데이터
data = {
    'name': ['Hong Gildong', 'Kim Cheolsu',
        'Lee Younghee', 'Park Jimin'],
    'Korean': [85, 92, 78, 95],
    'English': [90, 88, 82, 91],
    'Math': [78, 95, 88, 87]
}
df = pd.DataFrame(data)
print(df)
