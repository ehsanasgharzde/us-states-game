from turtle import Turtle


alignment = 'center'
font = ('Arial', 6, 'normal')

class Writer(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.speed(0)

    def gotolocation(self, xcor, ycor):
        self.goto(xcor, ycor)

    def updatescreen(self, state):
        self.write(f"{state}", False, alignment, font)
        