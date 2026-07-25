# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.14: for 문으로 파일을 한 줄씩 읽기

f = open('hello.txt', 'r')
for line in f:
    print(line, end='') # 줄바꿈 중복 방지
f.close()
