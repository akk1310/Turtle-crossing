FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level =1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-280,250)
        self.write(f"Level : {self.level}",align="left",font=FONT)

        
    def update(self):
        self.level +=1
        self.clear()
        self.write(f"Level : {self.level}",align="left",font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER",align="center",font=FONT)
    
    def reset(self):
        self.clear()
        self.level =1
        self.goto(-280,250)
        self.write(f"Level : {self.level}",align="left",font=FONT)



