# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제8장 예외 처리와 파일
# 코드 8.17: 학생 성적을 파일에 저장하고 읽기

# 성적 데이터를 파일에 저장
students = [
    'Hong Gildong,85,90,78',
    'Kim Cheolsu,92,88,95',
    'Lee Younghee,76,82,89'
]

with open('scores.txt', 'w') as f:
    for s in students:
        f.write(s + '\n')

# 파일에서 성적을 읽어 평균 계산
with open('scores.txt', 'r') as f:
    for line in f:
        data = line.strip().split(',')
        name = data[0]
        scores = [int(x) for x in data[1:]]
        avg = sum(scores) / len(scores)
        print(f'{name}: Average {avg:.1f}')
