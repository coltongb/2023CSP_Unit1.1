x = "o"
def stairs():
    global x
    for steps in range(5):
        print(x)
        x -= "o"

stairs()