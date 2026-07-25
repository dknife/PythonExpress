# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.12: replace()로 날짜·시간 변경

import datetime as dt

start_time = dt.datetime.now()
# 월을 12, 일을 25로 변경
new_time = start_time.replace(month = 12, day = 25)
print(new_time)
