# 알짜 파이썬 (강영민·박동규, 생능출판사) — 제10장 파이썬의 응용
# 코드 10.5: 코흐 눈송이 그리기

import turtle

def koch(t, length, depth):
    if depth == 0:
        t.forward(length)
        return
    length /= 3
    koch(t, length, depth - 1); t.left(60)
    koch(t, length, depth - 1); t.right(120)
    koch(t, length, depth - 1); t.left(60)
    koch(t, length, depth - 1)

def main():
    screen = turtle.Screen()
    screen.bgcolor('midnightblue')
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color('white')
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    for _ in range(3): # 눈송이 = 코흐 곡선 3개
        koch(t, 300, 4)
        t.right(120)
    turtle.done()

if __name__ == '__main__':
    main()
