# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.18: 파일 관련 예외 처리

try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('Error: File does not exist.')
except PermissionError:
    print('Error: Permission denied.')
