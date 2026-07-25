# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제11장 파이썬다운 코딩과 넘파이
# 코드 11.26: 넘파이 배열의 벡터화 연산

import numpy as np

student_mid = np.array([70, 85, 90, 75]) # 중간시험 점수
student_fin = np.array([90, 65, 70, 85]) # 기말시험 점수
student_sum = student_mid + student_fin
print('Total :', student_sum)
print('Average :', student_sum / 2)
