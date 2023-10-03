#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
variable = 10
variable -= 1
# Add a loop with a zero-iteration condition
while (variable < 10):
    painter.circle(100, 360, 6)

# Add an infinite loop
variable = 11
while (variable == 11):
    painter.circle(100, 360, 8)


wn = trtl.Screen()
wn.mainloop()