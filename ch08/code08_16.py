# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.16: pathlib의 Path 객체 사용하기

from pathlib import Path

p = Path('data') / 'scores.txt' # / 연산자로 경로 연결
print(p.exists()) # True/False
print(p.suffix) # '.txt'
print(p.stem) # 'scores'
print(p.parent) # PosixPath('data')

# 한 줄로 읽고 쓰기
p.parent.mkdir(exist_ok=True) # data 디렉토리가 없으면 생성
p.write_text('hello', encoding='utf-8')
text = p.read_text(encoding='utf-8')
