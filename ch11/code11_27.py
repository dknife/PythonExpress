# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제11장 파이썬다운 코딩과 넘파이
# 코드 11.27: 브로드캐스팅으로 보너스와 인상 계산

import numpy as np

sal = np.array([300, 360, 400, 380]) # 사원 4명의 급여
sal_bonus = sal + 100 # 각 급여에 상여금 100 더하기
sal_inc = sal * 1.2 # 각 급여를 20% 인상
print('After bonus:', sal_bonus)
print('After 20% raise:', sal_inc)
