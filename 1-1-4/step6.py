#   a114_divisible.py

# get two numbers from user
answer = input("give me a number")
answer2 = input("give me another number")

start_loop = 'y'
start_loop2 = 'y'

rem = int(answer) % int(answer2)
# loop while the numbers are not divisible (the remainder is not 0)
while (rem != 0):
    print("not divisible")
    answer = input("give me a number")
    answer2 = input("Give me another number")
    rem = int(answer) % int(answer2)
if (rem == 0):
    print("Divisible")
# inform user of result

# gather user input again

# inform user of result