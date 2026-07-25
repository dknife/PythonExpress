# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제7장 모듈 활용
# 코드 7.19: radians()로 각도를 라디안으로 변환

import math as m

# pi/2를 직접 사용 -- 올바른 결과
print(m.sin(m.pi/2.0)) # 1.0

# 원주율 값
print(m.pi) # 3.141592653589793

# 90도를 라디안으로 변환한 후 sin 사용
print(m.radians(90)) # 1.5707963267948966 (pi/2)
print(m.sin(m.radians(90))) # 1.0 -- 올바른 결과!
