# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.15: strftime()으로 날짜 문자열 포매팅

import datetime as dt

now = dt.datetime.now()
print(now.strftime('%Y-%m-%d')) # 2026-04-06
print(now.strftime('%B %d, %Y')) # April 06, 2026
print(now.strftime('%H:%M:%S')) # 14:30:25
