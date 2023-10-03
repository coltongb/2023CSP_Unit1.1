#   a114_while_guess.py

import turtle as trtl

# modify with your two favorite colors

wn = trtl.Screen()
height = 250 # the radius of the shape

painter = trtl.Turtle()
painter.speed(0)
painter.color("lime")

space = 1
angle = 150 # experiment with the shape
seg = int(360/angle)

while (painter.ycor() < height):
  if (space % 100 == 0):
    painter.fillcolor("purple")
    painter.color("purple")
  else:
    painter.fillcolor("lime")
    painter.color("lime")

  painter.right(angle)
  painter.forward(2*space + 10) # experiment
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()
  space += 1


wn.mainloop()