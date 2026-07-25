# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.5: 열 선택, 행 선택, 조건 필터링

import pandas as pd

# 코드 12.2의 df 준비
df = pd.DataFrame({
    'name': ['Hong Gildong', 'Kim Cheolsu',
        'Lee Younghee', 'Park Jimin'],
    'Korean': [85, 92, 78, 95],
    'English': [90, 88, 82, 91],
    'Math': [78, 95, 88, 87]
})

# 열 선택
print(df['name']) # 열 하나 -> Series
print(df[['name', 'Korean']]) # 열 여러 개 -> DataFrame

# 행 선택
print(df.loc[0]) # 레이블 인덱스 0의 행
print(df.iloc[0:2]) # 위치 기반 행 선택 (0~1)

# 조건 필터링
print(df[df['Korean'] >= 90]) # 국어 점수 90 이상인 학생
