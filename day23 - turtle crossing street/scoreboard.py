from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))
        
    def increase_score(self):
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
    
    
    