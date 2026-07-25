# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.10: date.today()로 연·월·일 추출

import datetime as dt

today = dt.date.today()
print(today) # 2026-04-06
print(today.year) # 2026
print(today.month) # 4
print(today.day) # 6
