#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 8
lngthlegs = 70
spacing = 180 / legs
spider.pensize(5)
n = 0
while (n < legs):
  if (n < 4):
    spider.goto(0,20)
    spider.setheading(spacing * n)
    spider.forward(lngthlegs)
  n = n + 1

  if (n > 4):
    spider.penup()
    spider.goto(0, 20)
    spider.pendown()
    spider.setheading(spacing * -n)
    spider.forward(lngthlegs)



spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()