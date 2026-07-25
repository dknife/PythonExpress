# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제12장 데이터 과학과 파이썬
# 코드 12.1: 인덱스가 있는 Series 만들기

import pandas as pd

# Series: 인덱스가 있는 1차원 데이터
s = pd.Series([85, 92, 78, 88],
    index=['Korean', 'English', 'Math', 'Science'])
print(s)
print(f'\nKorean score: {s["Korean"]}')
print(f'Mean: {s.mean():.1f}')
