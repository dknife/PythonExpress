# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.11: write()로 파일에 문자열 쓰기

f = open('hello.txt', 'w') # 1) 쓰기 모드로 파일 열기
f.write('Hello World!\n') # 2) 파일에 문자열 쓰기
f.write('Python file I/O\n')
f.close() # 3) 파일 닫기
