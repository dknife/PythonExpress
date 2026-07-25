# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.4: 탐색적 데이터 분석(EDA) 메소드

import pandas as pd

# 코드 12.2의 df 준비
df = pd.DataFrame({
    'name': ['Hong Gildong', 'Kim Cheolsu',
        'Lee Younghee', 'Park Jimin'],
    'Korean': [85, 92, 78, 95],
    'English': [90, 88, 82, 91],
    'Math': [78, 95, 88, 87]
})

print(df.head(2)) # 처음 2행
print(df.tail(2)) # 마지막 2행
print(df.shape) # (행 수, 열 수)
print(df.info()) # 열의 타입과 결측값 정보
print(df.describe()) # 수치형 열의 통계 요약
