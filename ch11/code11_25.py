# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제11장 파이썬다운 코딩과 넘파이
# 코드 11.25: 리스트로는 성적 평균을 구할 수 없음

student_mid = [70, 85, 90, 75] # 중간시험 점수
student_fin = [90, 65, 70, 85] # 기말시험 점수
student_sum = student_mid + student_fin
print(student_sum)
# student_sum / 2 # TypeError: unsupported operand type(s)
