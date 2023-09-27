# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle
painter.circle(50)

# move the turtle to another part of the screen
painter.pu()
painter.forward(200)

# add code here for an arc
painter.pd()
painter.circle(50, 180)

# move the turtle to another part of the screen
painter.pu()
painter.left(90)
painter.forward(200)

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.pd()
painter.circle(50, 180, 5)

# move the turtle to another part of the screen


# add code here to create a polygon of your choice using the circle method

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()