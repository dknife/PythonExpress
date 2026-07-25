# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.8: 가변 개수의 인자 받기

def average(*scores): # 모든 위치 인자를 튜플로 받음
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

print(average(80, 90, 100)) # 인자 3개
print(average(70, 85, 95, 100)) # 인자 4개
