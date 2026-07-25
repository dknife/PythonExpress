# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.15: with 문으로 안전하게 파일 처리

# with 문으로 파일 쓰기
with open('data.txt', 'w') as f:
    f.write('Name: Hong Gildong\n')
    f.write('Age: 20\n')
    f.write('Major: Computer Science\n')
# 블록이 끝나면 f.close()가 자동으로 호출됨

# with 문으로 파일 읽기
with open('data.txt', 'r') as f:
    for line in f:
        print(line, end='')
