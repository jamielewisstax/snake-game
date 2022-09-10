from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")

    def increase_score(self):
        self.clear()
        self.write(arg=f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)
        self.current_score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
