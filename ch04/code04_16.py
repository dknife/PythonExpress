# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.16: global 키워드로 전역변수 수정

count = 0 # 전역변수

def increment():
    global count # 전역변수 count 사용 선언
    count += 1

increment()
increment()
increment()
print('count =', count)
