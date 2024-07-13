import time
from turtle import Screen, Turtle
from player import Player  
from car_manager import CarManager  
from scoreboard import Scoreboard  

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
button = Turtle()
button.hideturtle()

screen.listen()
screen.onkey(player.move_up, "Up")

def create_button():
    button = Turtle()
    button.hideturtle()
    button.penup()
    button.goto(0, -100)
    button.color("white")
    button.write("Restart", align="center", font=("Courier", 24, "normal"))
    button.shape("square")
    button.shapesize(stretch_wid=2, stretch_len=5)
    button.showturtle()
    return button

def on_click(x, y):
    if -50 < x < 50 and -120 < y < -80:
        button.clear()
        button.hideturtle()
        game_loop()


def game_loop():
    global game_is_on
    game_is_on=True
    player.goto_start()
    car_manager.reset()
    scoreboard.reset()
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move()

        # Collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()
                global button
                button = create_button()
                screen.onscreenclick(on_click)
                # restart_button.showturtle()

        # Detect successful crossing
        if player.is_at_finish_line():
            player.goto_start()
            car_manager.lvl_up()
            scoreboard.update()




game_loop()

screen.mainloop()
