# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제10장 파이썬의 응용
# 코드 10.4: 재귀 나무 그리기

import turtle

ANGLE = 30 # 가지가 꺾이는 각도(단위: 도)
RATIO = 0.7 # 단계마다 줄어드는 길이 비율

def tree(t, length, depth):
    if depth == 0: # 종료 조건
        return
    t.forward(length) # 현재 가지 그리기
    t.left(ANGLE)
    tree(t, length * RATIO, depth - 1) # 왼쪽 부분 나무
    t.right(2 * ANGLE)
    tree(t, length * RATIO, depth - 1) # 오른쪽 부분 나무
    t.left(ANGLE)
    t.backward(length) # 시작 위치로 복귀

def main():
    screen = turtle.Screen()
    screen.bgcolor('white')
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color('saddlebrown')
    t.left(90) # 위쪽을 향하도록 회전
    t.penup()
    t.goto(0, -200)
    t.pendown()
    tree(t, 110, 9)
    turtle.done()

if __name__ == '__main__':
    main()
