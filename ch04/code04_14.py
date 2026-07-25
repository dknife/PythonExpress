# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제4장 함수와 입출력
# 코드 4.14: 지역변수와 전역변수의 범위

x1 = 10
x2 = 20
x3 = 30

def my_function() :
    global x1

    x1 = 1 # 전역변수 x1 (global로 선언됨)
    x2 = 2 # 지역변수 x2 (할당으로 생성)
    y1 = 40 # 지역변수
    y2 = 50

    print('inside function: ', x1, x2, x3, y1, y2)


my_function(); # 함수 호출, x1, x2, x3, y1, y2 출력
# 예상 출력: 1, 2, 30, 40, 50

print('outside function -')
print(x1, x2, x3) # 전역변수 x1, x2, x3
# 예상 출력: 1, 20, 30

print(y1, y2) # 지역변수 y1, y2는 접근 불가
# 예상 결과: NameError
