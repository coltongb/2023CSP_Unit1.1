import turtle as trtl

a = trtl.Turtle()
b = trtl.Turtle()
c = trtl.Turtle()
d = trtl.Turtle()

turtleList = [a, b, c, d]

x = -100
y = 0

for turtle in turtleList:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.right(30)
    x = x + 30


print(turtleList)

wn = trtl.Screen()
wn.mainloop()
