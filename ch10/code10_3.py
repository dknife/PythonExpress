# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제10장 파이썬의 응용
# 코드 10.3: turtle로 정사각형 그리기

import turtle

t = turtle.Turtle()
t.speed(0)
for _ in range(4):
    t.forward(120) # 한 변 그리기
    t.left(90) # 90도 회전
turtle.done()
