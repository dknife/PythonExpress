# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.9: 딕셔너리 형태의 키워드 인자 받기

def make_profile(**kwargs): # 키워드 인자를 딕셔너리로 받음
    for key, value in kwargs.items():
        print(f'{key}: {value}')

make_profile(name='Alice', age=20, job='Designer')
