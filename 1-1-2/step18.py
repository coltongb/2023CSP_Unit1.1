# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# set the pen and fill colors
# then draw a circle
painter.pencolor("green")
painter.fillcolor("pink")
painter.begin_fill()
painter.circle(150)
painter.end_fill()

# move the turtle to another part of the screen
painter.pu()
painter.goto(0, -120)


# change both the pen and fill colors
# then draw a polygon of your choice
painter.pd()
painter.pencolor("blue")
painter.fillcolor("purple")
painter.begin_fill()
painter.circle(50, 360, 8)
painter.end_fill()
# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()