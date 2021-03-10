from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle) :

    def __init__(self) :
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.high_score = int(data.read())
        self.bonus = 0;
        self.speed = 100
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self) :
        self.clear()
        self.write(f"Score: {self.score} Speed: {self.speed}% Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.high_score < self.score :
            self.high_score = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.bonus = 0
        self.speed = 100
        self.update_scoreboard()

    def game_over(self) :
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self, score, speed, bonus):
        self.score += score
        self.bonus += bonus
        self.speed = 100 + self.score + self.bonus
        self.clear()
        self.update_scoreboard()

    def getscore(self) :
        return self.score

    def getbonus(self):
        return self.bonus
