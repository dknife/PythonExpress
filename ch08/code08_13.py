# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.13: read, readline, readlines 비교

# 파일 전체를 하나의 문자열로 읽기
f = open('hello.txt', 'r')
content = f.read()
print(content)
f.close()

# 한 번에 한 줄씩 읽기
f = open('hello.txt', 'r')
line1 = f.readline() # 첫 번째 줄
line2 = f.readline() # 두 번째 줄
print(line1, line2)
f.close()

# 모든 줄을 리스트로 읽기
f = open('hello.txt', 'r')
lines = f.readlines() # ['Hello World!\n', 'Python file I/O\n']
print(lines)
f.close()
