# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.22: 로또 번호 생성기

import random as rd

lotto = rd.sample(range(1, 46), 6) # 1~45 중 6개 선택
lotto.sort()
print('This week lotto numbers:', lotto)
