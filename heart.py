import turtle
import time

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("pink")

t = turtle.Turtle()
t.hideturtle()
t.speed(1 )

def draw_heart(x, y, size, color, thickness):
  t.penup()
  t.goto(x, y)
  t.color(color)
  t.pensize(thickness)
  t.pendown()
  t.begin_fill()
  t.left(140)
  t.forward(size)
  for _ in range(200):
    t.right(1)
    t.forward(size * 0.009)
  t.left(140)
  for _ in range(200):
    t.right(1)
    t.forward(size * 0.009)
  t.forward(size)
  t.end_fill()
  t.setheading(0)

hearts = [
  (0, -150, 300, "#FF9999", 6),
  (0, -135, 270, "#FFCCCC", 6),
  (0, -120, 240, "#FFE6E6", 6),
  (0, -105, 210, "#FFCCCC", 6),
  (0, -90, 180, "#FF99CC",  6),
  (0, -75, 150, "#FFCCFF",  6),
  (0, -50, 100, "#FF6666",  6),
]

for heart in hearts:
  draw_heart(*heart)
  time.sleep(0.5)