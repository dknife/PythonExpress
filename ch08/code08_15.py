# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.15: with 문으로 안전하게 파일 처리

# with 문으로 파일 쓰기
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('이름: 홍길동\n')
    f.write('나이: 20\n')
    f.write('전공: 컴퓨터공학\n')
# 블록이 끝나면 f.close()가 자동으로 호출됨

# with 문으로 파일 읽기
with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
