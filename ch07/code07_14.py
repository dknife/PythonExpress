# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.14: timedelta로 100일 전후 날짜 계산

import datetime as dt

print('Today =', dt.datetime.now())
hundred = dt.timedelta(days = 100) # 100일

plus100day = dt.datetime.now() + hundred
print('100 days later =', plus100day)

minus100day = dt.datetime.now() - hundred
print('100 days ago =', minus100day)
