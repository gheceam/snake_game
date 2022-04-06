from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.screen = screen
        self.update_scoreboard()

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.color('white')
        self.hideturtle()
        self.penup()
        self.clear()
        self.goto(0, 390)
        self.write(arg=f"Score: {self.score}", align='center', font=("Courier", 18, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        
