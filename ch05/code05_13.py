# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제5장 리스트와 슬라이싱
# 코드 5.13: enumerate()로 인덱스와 값 함께 얻기

nations = ['Korea', 'China', 'India', 'Nepal']

for i, nation in enumerate(nations):
    print(f'No.{i}: {nation}')
