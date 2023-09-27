#   a113_circle_of_circles.py
#   Modify this code to draw a circle of circles
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")

for line in range(50):
    painter.stamp()
    painter.right(10)
    painter.forward(10)



wn = trtl.Screen()
wn.mainloop()