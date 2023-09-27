# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

painter.color(input("What is your favorite color?"))

radius = int(input("Choose a value for the radius"))
painter.circle(radius)

wn = trtl.Screen()
wn.mainloop()