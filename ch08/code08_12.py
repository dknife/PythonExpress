# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.12: writelines()로 여러 줄 한 번에 쓰기

lines = ['First line\n', 'Second line\n', 'Third line\n']
f = open('lines.txt', 'w')
f.writelines(lines)
f.close()
