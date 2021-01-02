import datetime
import time
import turtle

screen = turtle.Screen()
display = turtle.Turtle()

image = "4k-ultra-hd-background-toronto-canada-long-exposure-photogra.jpg"

while True:
    screen.title("NYE Countdown")
    # screen.bgcolor("pink")
    screen.bgpic("D:/pythonProject/Neural network/Snake/4k-ultra-hd-background-toronto-canada-long-exposure-photogra.gif")
    screen.setup(width=4000, height=2000, startx = 0, starty= 0)
    screen.tracer(0)

    hour = 23
    minute = 59
    seconds = 59
    time_now = datetime.datetime.now()

    countdown = f"{hour - time_now.hour:02d}:{minute - time_now.minute:02d}:{seconds - time_now.second:02d}"
    style = ('Arial', 120, "bold")
    display.color("white")
    display.write(countdown, font=style, align="center")

    time.sleep(1)
    screen.clear()

    if ((hour - time_now.hour) == 0) & ((minute - time_now.minute) == 0) & ((seconds - time_now.second) == 0):
        break

screen.bgpic("D:/pythonProject/Neural network/Snake/Blue-Fireworks-New-Year-2021-Wallpaper-72615.gif")
screen.setup(width=4000, height=2000, startx = 0, starty= 0)
screen.tracer(0)
screen.update()
countdown = "Happy New Year!!"
style = ('Arial', 120, "bold")
display.color("white")
display.write(countdown, font=style, align="center")
turtle.done()