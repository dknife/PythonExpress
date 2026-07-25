# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.6: Exception as e로 예외 내용 확인

try:
    b = 2 / 0
    a = 1 + 'hundred'
except Exception as e:
    print('error :', e)
