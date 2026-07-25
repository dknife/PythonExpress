# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.6: 별칭을 사용한 datetime 활용

import datetime as dt
start_time = dt.datetime.now()
xmas = start_time.replace(month=12, day=25)  # 반환값을 새 변수에 저장
print(xmas)
