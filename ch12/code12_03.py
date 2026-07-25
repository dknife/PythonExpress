# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.3: CSV 파일 읽기와 쓰기

import pandas as pd

# 코드 12.2의 df 준비
df = pd.DataFrame({
    'name': ['Hong Gildong', 'Kim Cheolsu',
        'Lee Younghee', 'Park Jimin'],
    'Korean': [85, 92, 78, 95],
    'English': [90, 88, 82, 91],
    'Math': [78, 95, 88, 87]
})

# DataFrame을 CSV 파일로 저장
df.to_csv('scores.csv', index=False, encoding='utf-8-sig')

# CSV 파일을 읽어 DataFrame 생성
df2 = pd.read_csv('scores.csv')
print(df2)
