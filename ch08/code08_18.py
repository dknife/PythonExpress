# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.18: 파일 관련 예외 처리

try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('오류: 파일이 없습니다.')
except PermissionError:
    print('오류: 접근 권한이 없습니다.')
