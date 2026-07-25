# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.15: 같은 이름의 전역·지역변수는 별개

x = 100 # 전역변수

def change_x():
    x = 999 # 지역변수 (전역변수와 별개)
    print('Inside function x:', x)

change_x()
print('Outside function x:', x) # 전역변수는 변하지 않음
