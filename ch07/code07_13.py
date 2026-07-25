# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.13: 크리스마스까지 남은 날 계산

import datetime as dt

today = dt.date.today()
print(f'Today is {today.year}/{today.month}/{today.day}.')

xMas = dt.datetime(2026, 12, 25)
gap = xMas - dt.datetime.now()

print(f'Christmas is {gap.days} days {gap.seconds // 3600} hours away.')
